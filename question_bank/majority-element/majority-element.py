# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了90.24% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了58.08% 的用户

解题思路：
    既然是多数元素，出现次数大于n//2。
    则排序后，n//2必然是多数元素
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]