# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了76.09% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.57% 的用户

解题思路：
    使用字典，记录每次
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        record = {i: float('inf') for i in 'abcdefghijklmnopqrstuvwxyz'}    # 用于记录各字符出现次数
        for a in A:
            record_now = {} # 当前单词各字符出现次数
            for i in a:
                if i in record_now:
                    record_now[i] += 1
                else:
                    record_now[i] = 1
            record = {i:min(n, record_now[i]) for i,n in record.items() if i in record_now} # 比较当前单词字符出现次数，更新record

        return [i for i,n in record.items() for _ in range(n)]