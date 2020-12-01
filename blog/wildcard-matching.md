Leetcode 44. 通配符匹配
<p>给定一个字符串&nbsp;(<code>s</code>) 和一个字符模式&nbsp;(<code>p</code>) ，实现一个支持&nbsp;<code>&#39;?&#39;</code>&nbsp;和&nbsp;<code>&#39;*&#39;</code>&nbsp;的通配符匹配。</p>


<pre>&#39;?&#39; 可以匹配任何单个字符。

&#39;*&#39; 可以匹配任意字符串（包括空字符串）。

</pre>



<p>两个字符串<strong>完全匹配</strong>才算匹配成功。</p>



<p><strong>说明:</strong></p>



<ul>

	<li><code>s</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母。</li>

	<li><code>p</code>&nbsp;可能为空，且只包含从&nbsp;<code>a-z</code>&nbsp;的小写字母，以及字符&nbsp;<code>?</code>&nbsp;和&nbsp;<code>*</code>。</li>

</ul>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong>

s = &quot;aa&quot;

p = &quot;a&quot;

<strong>输出:</strong> false

<strong>解释:</strong> &quot;a&quot; 无法匹配 &quot;aa&quot; 整个字符串。</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong>

s = &quot;aa&quot;

p = &quot;*&quot;

<strong>输出:</strong> true

<strong>解释:</strong>&nbsp;&#39;*&#39; 可以匹配任意字符串。

</pre>



<p><strong>示例&nbsp;3:</strong></p>



<pre><strong>输入:</strong>

s = &quot;cb&quot;

p = &quot;?a&quot;

<strong>输出:</strong> false

<strong>解释:</strong>&nbsp;&#39;?&#39; 可以匹配 &#39;c&#39;, 但第二个 &#39;a&#39; 无法匹配 &#39;b&#39;。

</pre>



<p><strong>示例&nbsp;4:</strong></p>



<pre><strong>输入:</strong>

s = &quot;adceb&quot;

p = &quot;*a*b&quot;

<strong>输出:</strong> true

<strong>解释:</strong>&nbsp;第一个 &#39;*&#39; 可以匹配空字符串, 第二个 &#39;*&#39; 可以匹配字符串 &quot;dce&quot;.

</pre>



<p><strong>示例&nbsp;5:</strong></p>



<pre><strong>输入:</strong>

s = &quot;acdcb&quot;

p = &quot;a*c?b&quot;

<strong>输出:</strong> false</pre>





 **难度**: Hard



 **标签**: 贪心算法、 字符串、 动态规划、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：832 ms, 在所有 Python3 提交中击败了71.51% 的用户
内存消耗：22.5 MB, 在所有 Python3 提交中击败了21.67% 的用户

解题思路：
    动态规划

    使用dp[i][j] 表示，p[i]之前部分与s[j]之前部分是否匹配
    例：
            ''  a   d   c   e   b
        ''  T   F   F   F   F   F
        *   T
        a   F
        *   F
        b   F

        表中，第一行第一类为空字符串，
        对于s中的空字符串，只有*或者''可以匹配。  当*时，dp[i][0] = dp[i-1][0]
        p中'' 只可以匹配''。则 dp[0][j] = False     j!=0


            ''  a   d   c   e   b
        ''  T   F   F   F   F   F
        *   T   T   T   T   T   T
        a   F   T   F   F   F   F
        *   F   T   T   T   T   T
        b   F   F   F   F   F   T

        对于表中其他位置，存在三种情况:
            1. p[i] == '*', 可以匹配一切，包含空字符串，
                则匹配空字符串时：dp[i][j] == dp[i-1][j]
                匹配1或多个字符时：  dp[i][j] == dp[i][j-1]
            2. p[i] == '?', 可匹配单个字符
                dp[i][j] == dp[i-1][j-1]
            3. 其他字符时，
                dp[i][j] == p[i]=s[j] and dp[i-1][j-1]
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_s = len(s)
        l_p = len(p)

        dp = [[False for _ in range(l_s+1)] for _ in range(l_p+1)]

        dp[0][0] = True
        for i in range(l_p):
            if p[i] == '*':
                dp[i+1][0] = dp[i][0]


        for i in range(l_p):
            for j in range(l_s):
                if p[i] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                elif p[i] == '?' and s[j] != '':
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]
</code></pre></div>
