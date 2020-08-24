# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了63.18% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了96.94% 的用户

解题思路：
    暴力解法。

"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2+1):  # 首先根据字符串长度判断可以被分为几段
            if n%i == 0:
                if s[:i] * (n//i) == s: # 判断字符串是否可以由当前分段组成
                    return True
        return False