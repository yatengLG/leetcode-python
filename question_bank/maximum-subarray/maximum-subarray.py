# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了77.21% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了43.31% 的用户

解题思路：
    动态规划
    从第一个元素开始
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
         i
    dp[i] = max(dp[i-1]+num[i], num[i])

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)