# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.39% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.32% 的用户

解题思路：
    栈
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for i in S:
            if i == '#':    # 如果是# ，出栈退格
                if s:
                    s.pop()
            else:           # 字母，进栈
                s.append(i)

        for i in T:
            if i == '#':
                if t:
                    t.pop()
            else:
                t.append(i)
        return s == t