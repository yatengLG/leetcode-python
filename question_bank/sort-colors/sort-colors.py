# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.58% 的用户
内存消耗：13.1 MB, 在所有 Python3 提交中击败了97.34% 的用户

解题思路：
    指针。将蓝色放到末尾，将红色放到起始。
    为避免无限循环，使用一个指针标记蓝色的放置位置
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0   # 指针，指向当前处理元素
        r = n-1 # 用于指向蓝色的放置位置。
        while index < r+1:
            # print(nums, index)
            if nums[index] == 0:
                nums.insert(0, nums.pop(index)) # 取出0，放到列表头部，index后移
                index += 1  # 指针+1
            elif nums[index] == 2:
                nums.insert(r, nums.pop(index)) # 取出2， 放到r指针指向位置，r前移。index不动
                r -= 1
            else:   # 1不处理， index后移
                index += 1