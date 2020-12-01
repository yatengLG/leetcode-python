Leetcode 343. 整数拆分
<p>给定一个正整数&nbsp;<em>n</em>，将其拆分为<strong>至少</strong>两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入: </strong>2

<strong>输出: </strong>1

<strong>解释: </strong>2 = 1 + 1, 1 &times; 1 = 1。</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入: </strong>10

<strong>输出: </strong>36

<strong>解释: </strong>10 = 3 + 3 + 4, 3 &times;&nbsp;3 &times;&nbsp;4 = 36。</pre>



<p><strong>说明: </strong>你可以假设&nbsp;<em>n&nbsp;</em>不小于 2 且不大于 58。</p>





 **难度**: Medium



 **标签**: 数学、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了97.80% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了63.31% 的用户

解题思路：
    动态规划
    例：
        2   1   1
        3   2   1
        4   2   2
        5   3   2
        6   3   3
        7   3   2   2
        8   3   3   2
        9   3   3   3
        10  3   3   2   2
        11  3   3   3   2
        12  3   3   3   3
    可看出，dp[i]=dp[i-3]*3  i>6
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[2:7] = [1,2,4,6,9]
        for i in range(7,n+1):
            dp[i] = dp[i-3] *3
        return dp[n]
</code></pre></div>
