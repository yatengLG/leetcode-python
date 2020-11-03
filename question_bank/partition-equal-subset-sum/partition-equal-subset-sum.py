# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1660 ms, 在所有 Python3 提交中击败了44.66% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了55.75% 的用户

解题思路：
    动态规划
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        if sum(nums) % 2 != 0:  # 奇数和 必不能拆分
            return False
        target = int(sum(nums)/2)   # 拆分后的和
        n = len(nums)
        dp = [0] * (target+1)   # 用于记录对应和能否实现
        dp[0] = 1   # 和为0必然可以

        for i in range(n):
            for j in range(target, -1, -1):
                if j+nums[i] <= target:
                    dp[j+nums[i]] = dp[j] or dp[j+nums[i]]  # 原先和+当前数值，即为新的和
            if dp[-1] == 1:
                return True
        return dp[-1] == 1


"""
超时
解题思路：
    回溯1
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()

        def backtrack(begin, current, target, used):
            if target == 0:
                return True
            if target < 0:
                return False

            for i in range(begin, len(nums)):
                if i > 1 and nums[i] == nums[i-1] and i-1 not in used:
                    continue
                if backtrack(i+1, current+[nums[i]], target-nums[i], used+[i]):
                    return True

        target = int(sum(nums) / 2)
        if target * 2 != sum(nums):
            return False

        if target < nums[-1]:
            return False

        if backtrack(0, [], target, []):
            return True
        else:
            return False


"""
超时
解题思路：
    回溯2
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        if max(nums) > target:
            return False

        nums.sort(reverse=True)
        def backtrack(current:int, nums:ist):
            if current == target:
                return True
            if current > target:
                return
            for i in range(len(nums)):
                if backtrack(current+nums[i], nums[i+1:]):
                    return True
            return False
        return backtrack(0, nums)