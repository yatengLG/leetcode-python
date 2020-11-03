# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了85.56% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.23% 的用户

解题思路：
    集合 去重
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        return [i for i in nums1 if i in nums2]