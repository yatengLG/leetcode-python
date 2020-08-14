# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了75.32% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.49% 的用户

解题思路：
    动态规划
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[] for _ in range(n)]

        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

"""
执行用时：40 ms, 在所有 Python3 提交中击败了96.92% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了90.98% 的用户

解题思路：
    动态规划，但是不记录每一步的值，改用比较更新的方式去寻找最大值
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        max_ = nums[0]
        for i in range(1, n):
            max_ = max(max_+nums[i], nums[i])
            if max_ > result:
                result = max_
        return result