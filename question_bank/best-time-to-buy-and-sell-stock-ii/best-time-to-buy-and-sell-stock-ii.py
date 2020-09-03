# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了39.51% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了58.55% 的用户

解题思路：
    贪心算法
    每次只求当前局部最优解。
    每当股价上升时，就将上升的幅度计入总利润， 最终得到的便是最大总利润
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        for i in range(n-1):
            result += max(prices[i + 1] - prices[i], 0)
        return result