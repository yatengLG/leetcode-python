Leetcode 714. 买卖股票的最佳时机含手续费
<p>给定一个整数数组&nbsp;<code>prices</code>，其中第&nbsp;<code>i</code>&nbsp;个元素代表了第&nbsp;<code>i</code>&nbsp;天的股票价格 ；非负整数&nbsp;<code>fee</code> 代表了交易股票的手续费用。</p>


<p>你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。</p>



<p>返回获得利润的最大值。</p>



<p><strong>注意：</strong>这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> prices = [1, 3, 2, 8, 4, 9], fee = 2

<strong>输出:</strong> 8

<strong>解释:</strong> 能够达到的最大利润:  

在此处买入&nbsp;prices[0] = 1

在此处卖出 prices[3] = 8

在此处买入 prices[4] = 4

在此处卖出 prices[5] = 9

总利润:&nbsp;((8 - 1) - 2) + ((9 - 4) - 2) = 8.</pre>



<p><strong>注意:</strong></p>



<ul>

	<li><code>0 &lt; prices.length &lt;= 50000</code>.</li>

	<li><code>0 &lt; prices[i] &lt; 50000</code>.</li>

	<li><code>0 &lt;= fee &lt; 50000</code>.</li>

</ul>





 **难度**: Medium



 **标签**: 贪心算法、 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：776 ms, 在所有 Python3 提交中击败了95.38% 的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了81.13% 的用户

解题思路：
    具体实现见代码注释
    参考了：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-shou-xu-fei-/
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        hold = -prices[0]   # 持有股票，需要花多钱
        for i in range(1, len(prices)):
            result = max(result, prices[i] + hold - fee)    # 第i天卖出的金钱，是前一天持有股票卖出的收益与当前持有金钱的最大值
            hold = max(hold, result-prices[i])  # 可以买入今天的股票，或者不不变
        return result
</code></pre></div>
