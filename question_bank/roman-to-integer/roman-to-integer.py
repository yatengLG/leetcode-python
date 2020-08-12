# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了85.72% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了72.20% 的用户

解题思路：
    罗马数字 存在两种情况：
        VI : 6 ，可以直接通过 5+1 计算。
        IX : 9 ，需要通过10-1计算
        通过对比相邻的罗马数字的大小，判断是属于哪种情况，然后计算
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'M':1000, 'D':500, 'C':100,
            'L':50, 'X':10, 'V':5, 'I':1
        }
        num = 0
        while len(s)>1:
            num_i = roman_dict[s[0]]
            num_j = roman_dict[s[1]]
            if num_i >= num_j:
                num = num + num_i
                s = s[1:]
            else:
                num = num + num_j - num_i
                s = s[2:]
        if s:
            num = num + roman_dict[s]
        return num