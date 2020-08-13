# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了87.93% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了55.99% 的用户

解题思路：
    动态规划
    由于不能挨着偷取，所以 当前偷取的值依赖于上上一个
        dp[i] == dp[i-2]+nums[i]
    当前偷取的最大值为
        dp[i] == max(dp[i-2]+nums[i], dp[i-1])
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        dp = [[] for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(dp)