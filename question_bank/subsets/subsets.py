# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.34% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了63.97% 的用户

解题思路：
    回溯
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtrack(i, current):  # 从第i个元素开始
            # print(current)
            result.append(current[:])
            if i >= n:  # 当遍历到
                return

            for j in range(i, n):
                current.append(nums[j])
                backtrack(j + 1, current)   # 下一个
                current.pop()               # 回溯

        backtrack(0, [])
        return result