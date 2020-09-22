# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了96.39% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了73.72% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')   # 去除右侧空格
        words = s.split(' ')    # 以空格划开单词
        return len(words[-1])   # 取最后一个单词的长度