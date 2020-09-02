# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了90.60% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了68.93% 的用户

解题思路：
    动态规划
    例：  1,17,5,10,13,15,10,5,16,8

            1     17    5    10     13    15    10    5     16    8
        ↗   0   ↗ 1 ↘ → 1   ↗ 3   ↗ 3   ↗ 3 ↘ → 3 ↘ → 3   ↗ 5 ↘ → 5
        ↘   0 ↗ → 0   ↘ 2 ↗ → 2 ↗ → 2 ↗ → 2   ↘ 4   ↘ 4 ↗ → 4   ↘ 6

        n   1     2     3     4     4     4     5     5     6     7

        使用dp[0][i]保存上升的结果，使用dp[1][i]表示下降的结果
        nums[i] > nums[i+1]时，上升
            dp[0][i] = dp[1][i-1] + 1   当前数值在上一个下降时的数值基础上+1
            dp[1][i] = dp[1][i-1]       当前数字下降等于前一个下降时的数值，保持不变
        nums[i] < nums[i+1]时，下降
            dp[0][i] = dp[0][i-1]       当前数值上升等于前一个数上升时的数值，保持不变
            dp[1][i] = dp[0][i-1] + 1   当前数字下降在前一个数上升的数值基础上+1
        nums[i] == nums[i+1]时，等于
            dp[0][i] = dp[0][i - 1]     上升下降均保持不变
            dp[1][i] = dp[1][i - 1]

"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[1][i] = dp[1][i - 1]
                dp[0][i] = dp[1][i - 1] + 1
            elif nums[i] < nums[i-1]:
                dp[1][i] = dp[0][i - 1] + 1
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = dp[1][i - 1]
        return max(dp[0][-1], dp[1][-1])+1