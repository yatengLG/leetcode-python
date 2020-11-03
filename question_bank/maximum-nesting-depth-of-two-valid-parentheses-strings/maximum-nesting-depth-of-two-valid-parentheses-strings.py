# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了98.57% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了10.68% 的用户

解题思路：
    先统计括号嵌套深度，然后进行分配
"""
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        d, max_d = 0, 0 # 当前深度，最大深度
        result = []
        for s in seq:
            max_d = max(d, max_d)
            if s == "(":    # 左括号
                d += 1      # 先深度+1
                result.append(d)    # 然后将当前括号深度添加到结果中
            if s == ")":    # 右括号
                result.append(d)    # 先将当前括号深度添加到结果中
                d -= 1              # 然后深度-1
        max_ = max_d//2 # 以深度，分为两部分
        result = [1 if r > max_ else 0 for r in result ] # 重新整理结果
        return result