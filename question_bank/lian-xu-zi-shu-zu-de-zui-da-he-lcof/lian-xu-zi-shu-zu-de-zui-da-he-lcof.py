# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了46.93% 的用户
内存消耗：23.3 MB, 在所有 Python3 提交中击败了5.02% 的用户
解题思路：
    动态规划
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[] for _ in range(n)]

        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


"""
执行用时：72 ms, 在所有 Python3 提交中击败了86.48% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了70.63% 的用户

解题思路：
    同动态规划，但不采用记录的方式，而是更新最大和.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        max_ = nums[0]
        record = nums[0]
        for i in range(1, n):
            record = max(record+nums[i], nums[i])
            if record > max_:
                max_ = record
        return max_