# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：468 ms, 在所有 Python3 提交中击败了85.90% 的用户
内存消耗：28 MB, 在所有 Python3 提交中击败了5.88% 的用户

解题思路：
    a^b = c
    c^a = b
    c^b = a
    先记录0~n的异或值
    然后，[q,p] 的异或值 = record[p] ^ record[q-1]
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        record = {-1:0}
        for i, a in enumerate(arr):
            record[i] = record[i-1] ^ arr[i]    # 记录每一位之前的异或值
        for q in queries:
            result.append(record[q[1]]^record[q[0]-1])  # 直接计算异或值   # a^b=c c^a=b c^b=a
        return result