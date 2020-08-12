# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：72 ms, 在所有 Python3 提交中击败了82.59% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.88%

解题思路：
    双指针，一个遍历字符串，一个记录当前子串起始点。
    使用字典存放字符串元素，
    若元素重复：
        更新子串起始点
        字典更新元素下标
        计算最大子串长度
    若不重复：
        字典登记元素，记录下标
        更新最大子串长度
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_, max_ = -1, 0
        record = {}
        for i, v in enumerate(s):
            if v not in record:
                record[v] = i
                max_ = max(i - start_, max_)
            else:
                start_ = max(record[v], start_)
                record[v] = i
                max_ = max(i - start_, max_)
        return max_


