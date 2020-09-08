# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了98.41% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了28.77% 的用户

解题思路：
    回溯
    先排序，指定起始元素下标，跳过重复元素
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # 先排序，便于处理重复元素
        n = len(nums)
        result = []
        def backtrack(i, current):  # 从第i个元素作为起始
            result.append(current[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:    # 如果遇到重复的元素则跳过
                    continue
                current.append(nums[j])
                backtrack(j + 1, current)   # 下一个元素
                current.pop()   # 回溯
        backtrack(0, [])
        return result