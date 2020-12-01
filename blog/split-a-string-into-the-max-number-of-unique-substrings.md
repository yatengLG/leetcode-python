Leetcode 1593. 拆分字符串使唯一子字符串的数目最大
<p>给你一个字符串 <code>s</code> ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。</p>


<p>字符串 <code>s</code> 拆分后可以得到若干 <strong>非空子字符串</strong> ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 <strong>唯一的</strong> 。</p>



<p>注意：<strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>s = &quot;ababccc&quot;

<strong>输出：</strong>5

<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;b&#39;, &#39;ab&#39;, &#39;c&#39;, &#39;cc&#39;] 。像 [&#39;a&#39;, &#39;b&#39;, &#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;cc&#39;] 这样拆分不满足题目要求，因为其中的 &#39;a&#39; 和 &#39;b&#39; 都出现了不止一次。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>s = &quot;aba&quot;

<strong>输出：</strong>2

<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;ba&#39;] 。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>s = &quot;aa&quot;

<strong>输出：</strong>1

<strong>解释：</strong>无法进一步拆分字符串。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>

	<p><code>1 &lt;= s.length&nbsp;&lt;= 16</code></p>

	</li>

	<li>

	<p><code>s</code> 仅包含小写英文字母</p>

	</li>

</ul>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    回溯+剪枝
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0

        def backtrack(s, current):

            if s == '':     # 如果字符串处理完成，则对比当前结果长度，更新结果
                if len(current) > self.result:
                    self.result = len(current)
                return

            if len(current) + len(s) <= self.result:    # 剪枝，如果当前剩余字符串长度+ 当前列表长度小于 最终结果，则跳出
                return

            for i in range(1, len(s)+1):    # 处理当前剩余的字符串
                if s[:i] not in current:
                    backtrack(s[i:], current+[s[:i]])

        backtrack(s, [])
        return self.result


"""
超出时间限制
思路：
    回溯，列举所有结果，然后对比
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = []

        def backtrack(s, current):
            print(s, current)
            if s == '':
                result.append(current[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] not in current:
                    backtrack(s[i:], current+[s[:i]])

        backtrack(s, [])
        result = [len(r) for r in result]
        return max(result)
</code></pre></div>
