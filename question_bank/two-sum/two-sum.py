# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了96.65% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.48% 的用户

解题思路：
    使用字典存储，快速查找
"""
class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        record = {}
        for i, v in enumerate(nums):
            a = target-v
            if a not in record:
                record[v] = i
            else:
                return [i, record[a]]
