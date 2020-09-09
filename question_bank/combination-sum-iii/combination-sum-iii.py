# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.19% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.93% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))   # 1~9
        result = []

        def backtrack(begin, current:list):

            if sum(current) == n and len(current) == k: # 如果和等于n, 且个数等于k， 则添加到最终结果中
                result.append(current[:])
                return

            if sum(current) > n or len(current) > k:    # 如果和大于9 或 当前列表长度大于k， 则跳出
                return

            for i in range(begin, 9):
                current.append(nums[i])
                backtrack(i+1, current) # 查看下一个
                current.pop()   # 回溯

        backtrack(0, [])
        return result