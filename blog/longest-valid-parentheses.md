Leetcode 32. 最长有效括号
<p>给定一个只包含 <code>&#39;(&#39;</code>&nbsp;和 <code>&#39;)&#39;</code>&nbsp;的字符串，找出最长的包含有效括号的子串的长度。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> &quot;(()&quot;

<strong>输出:</strong> 2

<strong>解释:</strong> 最长有效括号子串为 <code>&quot;()&quot;</code>

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> &quot;<code>)()())</code>&quot;

<strong>输出:</strong> 4

<strong>解释:</strong> 最长有效括号子串为 <code>&quot;()()&quot;</code>

</pre>





 **难度**: Hard



 **标签**: 字符串、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了86.20% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了5.47% 的用户

解题思路：
    动态规划
    ))()))(()()))((

    对于 i = ( ，dp[i] = 0
    对于 i = ) ，需要看前面一个
        如果 dp[i-1] 为0 ，则需看s[i-1]
            若s[i-1] = ( ,则匹配， 当前与前一个括号匹配，长度为2， 然后还需要看 i-2 是否是匹配的括号
                dp[i] = dp[i-2] + 2
            否则
                dp[i] = 0
        如果 dp[i-1] 不为0，则前面存在匹配的括号，此时，需查看 s[i-1-dp[i-1]]处字符，也就是前面匹配好的字符的前一个是很么括号
            若s[i-1-dp[i-1]] = (, 则匹配，
                dp[i] = dp[i-2-dp[i-1]] + 2 + dp[i - 1]
            否则
                dp[i] = 0

    在上述过程中，需判断 列表索引是否<0
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [[] for _ in range(n)]
        dp[0] = 0

        for i in range(1, n):
            if s[i] == '(':
                dp[i] = 0
            else:
                if dp[i - 1] == 0:  # 前一个字符是 ( 或 )
                    if s[i-1] == '(':   # 前一个字符是 (
                        if i - 2 > 0:   # 这里需要进行索引判断
                            dp[i] = 2 + dp[i - 1 - 1]
                        else:
                            dp[i] = 2
                    else:           # 前一个字符是 ), 不匹配
                        dp[i] = 0
                else:
                    if i - 1 - dp[i - 1] >= 0:  # 索引判断
                        if s[i - 1 - dp[i - 1]] == '(': # 匹配好的字符串前一个字符是 (
                            if i - 2 - dp[i - 1] > 0:
                                dp[i] = dp[i - 1] + 2 + dp[i - 1 - dp[i - 1] - 1]
                            else:
                                dp[i] = dp[i - 1] + 2
                        else:                           # 匹配好的字符串前一个字符是 )
                            dp[i] = 0
                    else:
                        dp[i] = 0
        return max(dp)

"""
另附一份精简后的代码
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [[] for _ in range(n)]
        dp[0] = 0

        for i in range(1, n):
            if s[i] == ')' and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                if i - 2 - dp[i - 1] > 0:
                    dp[i] = dp[i - 1] + 2 + dp[i - 1 - dp[i - 1] - 1]
                else:
                    dp[i] = dp[i - 1] + 2
            else:
                dp[i] = 0
        return max(dp)
</code></pre></div>
