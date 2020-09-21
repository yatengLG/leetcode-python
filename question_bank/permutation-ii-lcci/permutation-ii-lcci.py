# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了89.10% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了43.09% 的用户

解题思路：
    回溯
    更新当前剩余字符串，跳过当前字符串中已经处理过的元素
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        result = []
        def backtrack(s, current):  # 当前剩余字符串，当前字符串
            if s == '':
                result.append(current[:])
                return
            for i in range(len(s)):
                if i > 0 and s[i] in s[:i]: # 跳过当前剩余字符串中重复的元素
                    continue
                backtrack(s[:i]+s[i+1:], current+s[i])
        backtrack(S, '')
        return result