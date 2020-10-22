# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了81.82% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了18.18% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p, q = 0, 0     #指针
        while p < len(name) and q < len(typed):
            if name[p] == typed[q]: # 如果对应位置匹配，指针同时后移，匹配下一个
                p += 1
                q += 1
            else:
                if q > 0 and typed[q-1] == typed[q]:    # 如果typed存在连击，匹配下一个
                    q += 1
                else:   # 不存在连击，返回False
                    return False
        if p >= len(name):   # name匹配完
            if q >= len(typed):  # typed 也匹配完
                return True
            else:
                while q < len(typed):   # 若typed没有匹配完，且后续连击，返回True
                    if typed[q] != typed[q-1]:  # 若不存在连击，则返回False
                        return False
                    q += 1
                return True
        else:
            return False