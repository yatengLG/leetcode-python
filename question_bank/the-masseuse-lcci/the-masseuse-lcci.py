# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：16 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.92% 的用户

解题思路：
    动态规划
    由于中间需要休息，也就是最少需要间隔一个元素，所以在计算当前点时，需要跳过一个元素往前看
    但由于在计算时，必须相隔一个元素，这样就造成相领两个元素的值大小不定。
    这样在计算时，就必须，跳过前一个元素，比较之前两个元素的大小
    dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
"""

class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[:2])
        if n == 2:
            return max(nums[0]+nums[2], nums[1])

        dp = [[] for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        dp[2] = max(nums[0]+nums[2], nums[1])

        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

        return max(dp[-2:])