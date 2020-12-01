# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了74.31% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了12.21% 的用户

解题思路：
    二分查找，寻找target在nums中的位置
    以找到的target值，向两侧扩张
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找，寻找target
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                break
            elif nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        # 从找到的值，向两侧寻找
        if l <= r and nums[(l + r) // 2] == target:
            l, r = (l + r) // 2, (l + r) // 2
            while l-1 >= 0 and nums[l-1] == target:
                l -= 1
            while r+1 <= len(nums)-1 and nums[r+1] == target:
                r += 1
            return [l,r]
        else:
            return [-1, -1]