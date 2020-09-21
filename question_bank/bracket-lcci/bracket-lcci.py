# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了85.42% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了29.31% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(l, r, current):   # 剩余左括号个数，剩余右括号个数，当前括号组合
            if l == 0 and r == 0:       # 如果括号都用完，则添加到最终结果中
                result.append(current[:])
                return
            if l > r or l < 0 or r < 0: # 如果剩余左括号比剩余右括号多，或左括号用完，或右括号用完，跳出
                return
            backtrack(l-1, r, current+'(')  # 使用一个左括号
            backtrack(l, r-1, current+')')  # 使用一个右括号
        backtrack(n, n, '')
        return result