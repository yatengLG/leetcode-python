# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了73.57% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了70.71% 的用户

解题思路：
    回溯+剪枝
"""
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        result = []
        n = len(A)
        A.sort()    # 排序，便于重复元素剪枝
        def backtrack(index, current, used):    # 当前节点索引， 当前列表， 使用用的索引
            if len(current) == n and current not in result: # 如果当前列表包含了所有A元素，添加到最终结果中
                result.append(current)
                return

            for i in range(n):
                if i not in used:   # 循环A，对于没有使用过的元素
                    num = (A[index] + A[i]) ** 0.5  # 计算开方
                    if i > 0 and A[i] == A[i-1] and i-1 not in used:    # 重复元素剪枝
                        continue
                    if int(num) == num: # 如果是完全平方数，则将A[i]添加到当前列表
                        backtrack(i, current+[A[i]], used+[i])  # 把index更新为i

        for index in range(n):  # 已不同下标开始
            if index > 0 and A[index] == A[index-1]:    # 跳过相同元素
                continue
            backtrack(index, [A[index]], [index])

        return len(result)