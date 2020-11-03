# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.66% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.64% 的用户

解题思路：
    统计未匹配的左右括号。
    具体实现见代码注释
"""
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l, r = 0, 0     # 左括号，右括号未匹配数统计
        for s in S:
            if s == '(':    # 如果是左括号，则左括号+1
                l += 1
            if s == ')':    #
                if l < 1:   # 左括号匹配完后，未匹配的右括号+1
                    r += 1
                else:
                    l -= 1  # 如果有多余的左括号, 则消耗一个左括号
        return l+r  # 返回未匹配的左括号和右括号的总和