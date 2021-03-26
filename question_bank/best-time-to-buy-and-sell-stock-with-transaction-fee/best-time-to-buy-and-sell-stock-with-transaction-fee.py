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