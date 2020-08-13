# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了91.41% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了82.66% 的用户

解题思路：
    动态规划
    初始点可以是第一个或者第二个，单独处理这种情况
    对于大于三的点，其可以由第二个+1，也可以由第一个+2，取最小值即可
    dp[i] = min(dp[i-1], dp[i-2])

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:      # 对于单个元素，直接返回
            return cost[0]
        if n == 2:      # 两个元素，可经第一个，直接到顶；也可经第二个直接到顶
            return min(cost[0],cost[1])

        dp = [[] for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i] # 大于三的元素，依赖于前一个和前两个元素的值，最后加上本身的值
        cost = min(dp[-1], dp[-2])  # 最后需要处理，可经倒数第一个元素到顶，也可经倒数第二个元素到顶

        return cost