# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：244 ms, 在所有 Python3 提交中击败了28.18% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了13.10% 的用户

解题思路：
    模拟竖式乘法运算，逻辑与列竖式相同
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i, val1 in enumerate(num1[::-1]):
            for j, val2 in enumerate(num2[::-1]):
                result += int(val1) * int(val2) * 10 ** (i + j)
        return str(result)

"""
执行用时：124 ms, 在所有 Python3 提交中击败了60.60% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了17.70% 的用户

解题思路：
    优化后，速度大幅提升，使用数组存储每次的计算结构，然后求和    
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        record = [0]*(len(num1)+len(num2))
        for i, val1 in enumerate(num1[::-1]):
            for j, val2 in enumerate(num2[::-1]):
                record[i+j] += int(val1) * int(val2)

        result = 0
        for power, val in enumerate(record):
            result += val*10**power

        return str(result)