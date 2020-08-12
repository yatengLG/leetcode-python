# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了88.61% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了82.05% 的用户

解题思路：
    根据题意，不需要主动删除重复元素，只需将不重复元素前移即可
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i, value in enumerate(nums):
            if value == val:
                pass
            else:
                nums[index] = value
                index += 1
        return index