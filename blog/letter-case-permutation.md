Leetcode 784. 字母大小写全排列
<p>给定一个字符串<code>S</code>，通过将字符串<code>S</code>中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。</p>


<p>&nbsp;</p>



<pre><strong>示例：</strong>

<strong>输入：</strong>S = &quot;a1b2&quot;

<strong>输出：</strong>[&quot;a1b2&quot;, &quot;a1B2&quot;, &quot;A1b2&quot;, &quot;A1B2&quot;]



<strong>输入：</strong>S = &quot;3z4&quot;

<strong>输出：</strong>[&quot;3z4&quot;, &quot;3Z4&quot;]



<strong>输入：</strong>S = &quot;12345&quot;

<strong>输出：</strong>[&quot;12345&quot;]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>S</code>&nbsp;的长度不超过<code>12</code>。</li>

	<li><code>S</code>&nbsp;仅由数字和字母组成。</li>

</ul>





 **难度**: Medium



 **标签**: 位运算、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了93.23% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.35% 的用户

解题思路：
    回溯
    遍历字符串，如果是字母，则改写其大小写，并将改写前和改写后的整条字符串均添加到最后结果中
    具体实现见代码注释
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        result = []
        def backtrack(begin, S):    # 指定一个起始，与当前字符串S
            result.append(S[:])     # 因为是所有的满足条件的字符串，所以可以直接添加到最终结果
            if begin == n:  # 超出字符串长度则跳出
                return
            for i in range(begin, n):   # 从指定的起始位置开始，查看当前字符串
                if S[i].isalpha():
                    if 'a' <= S[i] <= 'z':  # 如果是小写，则改成大写
                        backtrack(i+1, S[:i]+S[i].upper()+S[i+1:])
                    elif 'A' <= S[i] <= 'Z':    # 是大写，则改成小写
                        backtrack(i+1, S[:i]+S[i].lower()+S[i+1:])

        backtrack(0, S)
        return result</code></pre></div>
