# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了77.59% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了62.39% 的用户

解题思路：
    栈，使用列表模拟进栈出栈操作
"""

class Solution:
    def isValid(self, s: str) -> bool:
        l_r = {'(': ')', '{': '}', '[': ']'}
        record = []
        for c in s:
            if c == ' ':
                continue
            if c == '(':
                record.append('(')
            elif c == '[':
                record.append('[')
            elif c == '{':
                record.append('{')
            else:
                if record:
                    r_ = record.pop()
                    if l_r[r_] != c:
                        print(r_, '==', c)
                        return False
                else:
                    return False
        if record == []:
            return True
        else:
            return False