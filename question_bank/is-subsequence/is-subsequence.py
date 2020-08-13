# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了39.48% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了88.49% 的用户

解题思路：
    双指针法
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t) :
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False


