Leetcode 309. 最佳买卖股票时机含冷冻期
<p>给定一个整数数组，其中第<em>&nbsp;i</em>&nbsp;个元素代表了第&nbsp;<em>i</em>&nbsp;天的股票价格 。​</p>


<p>设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:</p>



<ul>

	<li>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</li>

	<li>卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。</li>

</ul>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [1,2,3,0,2]

<strong>输出: </strong>3 

<strong>解释:</strong> 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]</pre>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了76.60% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了10.86% 的用户

解题思路：
    动态规划
    在处理该问题时，主要存在三种状态，买， 卖， 冷冻期。必须在不持有情况下才可以买进，在持有状态下才可以卖出。
    将该问题分为以下三种情况：
        1. 不持有股票
            可以为前一天不持有，或前一天持有卖出
        2. 持有股票
            可以为前一天持有，或前一天为冷冻期，今天买入
        3. 冷冻期
            冷冻期为早一天刚出售股票，今天不能买入，此时利润与前一天不持有时相同。
                * 若早一天不持有是由再前一天不持有状态而来，那么利润不会有变化，所以可以同一逻辑处理。

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][1] = -prices[0]               # 第一天持有
        dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])    # 第二天不持有：(第一天不持有， 第一天持有卖出)
        dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])    # 第二天持有：(第一天持有，第一天不持有买进)
        dp[1][2] = dp[0][0]                             # 冷却期当天，利润与前一天不持有股票利润一致
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])      # 不持有股票的情况：(原本不持有，早一天持有卖出)
            dp[i][1] = max(dp[i-1][1], dp[i-1][2] - prices[i])      # 持有股票的情况：(原本持有，原本不持有买进，需要注意的是买进时，必须是冷冻期之后才可以)
            dp[i][2] = dp[i-1][0]                                   # 冷冻期与前一天不持有时利润一致
        return max(dp[-1])

</code></pre></div>
