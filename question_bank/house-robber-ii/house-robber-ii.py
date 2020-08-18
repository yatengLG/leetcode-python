# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.16% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了52.73%

解题思路：
    由于头尾相连，将环拆开，[1:]与[:-1] 单独处理，并取最大值
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def f(nums):
            pre, cur = 0, 0
            for num in nums:
                cur, pre = max(pre+num, cur), cur
            return cur
        return max(f(nums[1:]), f(nums[:-1]))