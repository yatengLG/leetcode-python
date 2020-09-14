# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.81% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了92.02% 的用户

解题思路：
    动态规划

    以 nums = [1,2,4] target = 7为例

    target:     1       2       3       4       5       6       7
    dp:         1       2       3       6       10      18      31

        dp[i] = dp[i-1] + dp[i-2] + dp[i-4]
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target+1)]
        dp[0] = 1

        for t in range(1, target+1):

            for num in nums:
                if t  < num:
                    break
                else:
                    dp[t] += dp[t-num]

        return dp[target]