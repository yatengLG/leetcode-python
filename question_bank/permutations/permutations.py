# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了41.92% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了62.85% 的用户

解题思路：
    回溯
    具体实现见代码
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []     # 最终结果

        def backtrack(current:list, used:list): # 当前列表，用于记录使用过的数组的列表
            if len(current) >= n:
                result.append(current[:])
                return

            for i in range(n):  # 循环每个数字作为起始
                if nums[i] not in used: # 如果当前数字没有使用过
                    current.append(nums[i]) # 加入当前列表
                    used.append(nums[i])    # 记录为已使用
                    backtrack(current, used)    # 下一个数字
                    current.pop()   # 回溯
                    used.pop()

        backtrack([], [])

        return result