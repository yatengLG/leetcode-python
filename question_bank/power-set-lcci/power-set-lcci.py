# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了96.84% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了24.26% 的用户

解题思路：
    回溯
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 先排序，方便处理重复元素
        n = len(nums)
        result = []

        def backtrack(index, current):
            result.append(current[:])
            if index >= n:
                return
            for i in range(index, n):
                if i>0 and nums[i] == nums[i-1]:    # 跳过重复元素
                    continue
                backtrack(i+1, current+[nums[i]])
        backtrack(0, [])
        return result