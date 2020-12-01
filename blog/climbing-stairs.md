Leetcode 70. 爬楼梯
<p>假设你正在爬楼梯。需要 <em>n</em>&nbsp;阶你才能到达楼顶。</p>


<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>



<p><strong>注意：</strong>给定 <em>n</em> 是一个正整数。</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong> 2

<strong>输出：</strong> 2

<strong>解释：</strong> 有两种方法可以爬到楼顶。

1.  1 阶 + 1 阶

2.  2 阶</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong> 3

<strong>输出：</strong> 3

<strong>解释：</strong> 有三种方法可以爬到楼顶。

1.  1 阶 + 1 阶 + 1 阶

2.  1 阶 + 2 阶

3.  2 阶 + 1 阶

</pre>





 **难度**: Easy



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了95.41% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了47.58% 的用户

解题思路：
    动态规划
    每次只能爬1层 或 爬2层。
    例：5层， 可以由3层 +2 到达、也可以4层+1 到达。
    所以5层的方法数 = 3层的方法数 + 4层的方法数
    dp[i] = dp[i-1] + dp[i-2]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [[] for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
</code></pre></div>
