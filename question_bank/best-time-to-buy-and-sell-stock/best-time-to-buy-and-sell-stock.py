# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了95.92% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了41.17% 的用户

解题思路：
    记录当前最小值，作为买入时机，依次更新买入时机并计算利润
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if buy > price:
                buy = price
            else:
                profit = max((price-buy), profit)
        return profit