# -*- coding: utf-8 -*-
# @Author  : LG
"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.24% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了97.09% 的用户

解题思路：
    使用双指针分别指向两字符串
    具体实现见代码注释
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        len_i, len_j = len(haystack), len(needle)
        record = -1         # 初始化为-1， 用于记录字符相等时的下标
        i, j = 0, 0         # 双指针
        while i < len_i:    # 循环遍历字符串haystack
            if haystack[i] == needle[j]:    # 若haystack当前下标i指向的字符与needle字符串当前下标j所指向的字符相等
                record = i  # record记录当前i下标
                j += 1      # 后移needle字符串下标
            else:
                i = i-j     # 否则，将i下标移动到之前开始匹配的后一项
                j = 0       # j指针指向needle第一个字符
                record = -1 # record归-1
            if j > len_j-1: # 如needle字符串遍历完毕，则跳出循环
                break
            else:
                record = -1
            i += 1
        if record > 0:  # 匹配成功时，record指向匹配字符串的末尾，需要移动到匹配字符串的开始
            record -= len_j-1
        return record