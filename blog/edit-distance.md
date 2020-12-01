Leetcode 72. 编辑距离
<p>给你两个单词&nbsp;<em>word1</em> 和&nbsp;<em>word2</em>，请你计算出将&nbsp;<em>word1</em>&nbsp;转换成&nbsp;<em>word2 </em>所使用的最少操作数&nbsp;。</p>


<p>你可以对一个单词进行如下三种操作：</p>



<ol>

	<li>插入一个字符</li>

	<li>删除一个字符</li>

	<li>替换一个字符</li>

</ol>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1：</strong></p>



<pre><strong>输入：</strong>word1 = &quot;horse&quot;, word2 = &quot;ros&quot;

<strong>输出：</strong>3

<strong>解释：</strong>

horse -&gt; rorse (将 &#39;h&#39; 替换为 &#39;r&#39;)

rorse -&gt; rose (删除 &#39;r&#39;)

rose -&gt; ros (删除 &#39;e&#39;)

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入：</strong>word1 = &quot;intention&quot;, word2 = &quot;execution&quot;

<strong>输出：</strong>5

<strong>解释：</strong>

intention -&gt; inention (删除 &#39;t&#39;)

inention -&gt; enention (将 &#39;i&#39; 替换为 &#39;e&#39;)

enention -&gt; exention (将 &#39;n&#39; 替换为 &#39;x&#39;)

exention -&gt; exection (将 &#39;n&#39; 替换为 &#39;c&#39;)

exection -&gt; execution (插入 &#39;u&#39;)

</pre>





 **难度**: Hard



 **标签**: 字符串、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：216 ms, 在所有 Python3 提交中击败了47.71% 的用户
内存消耗：31.7 MB, 在所有 Python3 提交中击败了5.07% 的用户

解题思路：
    动态规划

    例：
            ''  h   o   r   s   e
        ''  0   1   2   3   4   5
        r   1   1   2   2   3   4
        o   2   2   1   2   3   4
        s   3   3   2   2   2   3

        当 world2[i] == world1[j]时， dp[i][j] = dp[i-1][j-1]
        当 world2[i] != world1[j]时，
            1. dp[i][j] = dp[i-1][j]+1      可通过world2[i-1] 删除一个元素得到 world1[j]
            2. dp[i][j] = dp[i-1][j-1]+1    可通过world2[i]， world1[j] 替换最后一个元素得到
            3. dp[i][j] = dp[i][j-1]+1      可通过world2[i] 插入一个元素得到 world1[j-1]，
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[[] for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        dp[0] = list(range(m+1))

        for i in range(n):
            for j in range(m):
                if word2[i] == word1[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        return dp[-1][-1]</code></pre></div>
