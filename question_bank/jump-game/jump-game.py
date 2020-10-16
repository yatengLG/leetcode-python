# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了83.73% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了9.98% 的用户

解题思路：
    当前点能到达的最远点决定了当前点能到达的范围
    只有能到达的最远点比结尾远，就一定能到达
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0 # 能到达的最远点
        for i, num in enumerate(nums):
            if i <= far:    # 如果当前点，现在能到达
                far = max(far, i+num)   # 更新能到达的最远点
        return far >= i # 比较能到达的最远点与列表长度