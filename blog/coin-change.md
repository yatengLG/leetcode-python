Leetcode 322. 零钱兑换
<p>给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回&nbsp;<code>-1</code>。</p>


<p>&nbsp;</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入: </strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>

<strong>输出: </strong><code>3</code> 

<strong>解释:</strong> 11 = 5 + 5 + 1</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入: </strong>coins = <code>[2]</code>, amount = <code>3</code>

<strong>输出: </strong>-1</pre>



<p>&nbsp;</p>



<p><strong>说明</strong>:<br>

你可以认为每种硬币的数量是无限的。</p>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1668 ms, 在所有 Python3 提交中击败了45.86% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了67.60% 的用户

解题思路：

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            record = []
            for coin in coins:
                if i - coin == 0:
                    dp[i] = 1
                    break
                if i - coin > 0 and dp[i-coin] >= 0:
                    record.append(dp[i-coin])
            if record != [] and dp[i] != 1:
                dp[i] = min(record) + 1
        return dp[-1]


"""
执行用时：1556 ms, 在所有 Python3 提交中击败了62.00% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了28.90% 的用户

解题思路：
    精简下代码,并将两次循环的顺序调换了下，第二次循环从当前硬币币值开始
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1</code></pre></div>
