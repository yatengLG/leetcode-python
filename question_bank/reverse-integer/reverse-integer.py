# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了44.37% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了75.16% 的用户

解题思路：
    判断输入整数正负并记录，依次取出输入整数的最后一位，存入列表，再反序取出
"""
class Solution:
    def reverse(self, x: int) -> int:

        if x<0:
            negative = -1
            x = -x
            max_ = 2**31
        else:
            max_ = 2**31-1
            negative = 1
        record = []
        print(max_)
        while x != 0:
            record.append(x%10)
            x = x//10

        num = 0
        for i, v in enumerate(record[::-1]):
            num += v*10**i
            if num > max_:
                return 0
        return num*negative