# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了95.14% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.42% 的用户

解题思路：
    先统计每个数出现的次数
    然后查看次数是否存在重复
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        record = {}
        for a in arr:
            if a in record:
                record[a] += 1
            else:
                record[a] = 1
        return len(record.values()) == len(set(record.values()))