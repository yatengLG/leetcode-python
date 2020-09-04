# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了91.06% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了42.14% 的用户

解题思路：
    递归
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)
        def backtrack(index, target, current):  # 递归，开始的下标，目标值，当前数组
            for i in range(index, n):
                num = candidates[i]
                if num == target:
                    result.append(current+[num])    # 当前数组下 某值与目标值相等，则加入到结果中
                elif num > target:  # 数值大于目标值，则跳出
                    return
                else:               # 小于目标值，下一层
                    backtrack(i, target-num, current+[num])
        backtrack(0, target, [])
        return result