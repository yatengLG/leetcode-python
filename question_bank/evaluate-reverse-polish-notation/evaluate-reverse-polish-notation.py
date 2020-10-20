# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.20% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    栈
    当遇到+-*/时，出栈两个，进行计算后，将结果入栈
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []
        for token in tokens:
            if token == '+':
                b = record.pop()    # 出栈两个数字，分别作为a,b
                a = record.pop()
                cal = int(int(a) + int(b))  # 计算获得结果，并将计算结果入栈
                record.append(cal)
            elif token == '-':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) - int(b))
                record.append(cal)
            elif token == '*':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) * int(b))
                record.append(cal)
            elif token == '/':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) / int(b))
                record.append(cal)
            else:
                record.append(token)
        return int(record.pop())