# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.93% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了30.41% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0   # 当前指针
        index = 0   # 用于记录插入位置
        while i < len_nums:
            if nums[i] != 0:    # 不为0 时， 将当前数与插入位置数交换
                nums[index], nums[i] = nums[i], nums[index]
                index += 1  # 插入位置后移
            i += 1 # 处理下一个数