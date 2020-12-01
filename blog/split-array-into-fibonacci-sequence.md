Leetcode 842. 将数组拆分成斐波那契序列
<p>给定一个数字字符串 <code>S</code>，比如 <code>S = &quot;123456579&quot;</code>，我们可以将它分成斐波那契式的序列 <code>[123, 456, 579]</code>。</p>


<p>形式上，斐波那契式序列是一个非负整数列表 <code>F</code>，且满足：</p>



<ul>

	<li><code>0 &lt;= F[i] &lt;= 2^31 - 1</code>，（也就是说，每个整数都符合 32 位有符号整数类型）；</li>

	<li><code>F.length &gt;= 3</code>；</li>

	<li>对于所有的<code>0 &lt;= i &lt; F.length - 2</code>，都有 <code>F[i] + F[i+1] = F[i+2]</code> 成立。</li>

</ul>



<p>另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。</p>



<p>返回从 <code>S</code> 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 <code>[]</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>&quot;123456579&quot;

<strong>输出：</strong>[123,456,579]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入: </strong>&quot;11235813&quot;

<strong>输出: </strong>[1,1,2,3,5,8,13]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入: </strong>&quot;112358130&quot;

<strong>输出: </strong>[]

<strong>解释: </strong>这项任务无法完成。

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>&quot;0123&quot;

<strong>输出：</strong>[]

<strong>解释：</strong>每个块的数字不能以零开头，因此 &quot;01&quot;，&quot;2&quot;，&quot;3&quot; 不是有效答案。

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入: </strong>&quot;1101111&quot;

<strong>输出: </strong>[110, 1, 111]

<strong>解释: </strong>输出 [11,0,11,11] 也同样被接受。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= S.length&nbsp;&lt;= 200</code></li>

	<li>字符串 <code>S</code> 中只含有数字。</li>

</ol>





 **难度**: Medium



 **标签**: 贪心算法、 字符串、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：148 ms, 在所有 Python3 提交中击败了35.57% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了36.81% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def backtrack(S, current):
            if S == '' and len(current) > 2:    # 字符串均处理完，且当前序列长度大于2， 返回最终结果
                return True

            if S == '': # 当字符串处理完时，跳出
                return

            for i in range(1, len(S)+1): # 遍历当前字符串
                if (S[0] == '0' and i == 1) or (S[0] != '0'):   # 排除以0 开头的非0数， 如 01 02 等
                    if int(S[:i]) < (2**31-1) and (len(current) < 2 or int(S[:i]) == int(current[-1]) + int(current[-2])):  # 数字限制；长度判断，如长度小于2，直接添加，如长度大于2，需判断和
                        current.append(S[:i])
                        if backtrack(S[i:], current):
                            return current
                        current.pop()

        result = backtrack(S, [])
        if result:
            return result
        else:
            return []</code></pre></div>
