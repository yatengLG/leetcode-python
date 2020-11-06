# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了31.59% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.69% 的用户

解题思路：
    位运算-异或
    a ^ 0 = a
    a ^ a = 0
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)