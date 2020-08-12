# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了93.52% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了79.33% 的用户

解题思路：
    依次取出数字的最后一位进行判断
    罗马数字分几种情况：
        1~3:    III
        4:      IV
        5:      V
        6-8:    VIII
        9:      IX
    用列表分别存储 1 5 10在不同位上的表示，即：[[1, 5, 10], [10, 50, 100], [100, 500, 1000], [1000]]
    在不同位时，用不同位的表示依照罗马数字分情况处理即可
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = [
            ['I', 'V', 'X',],
            ['X', 'L', 'C'],
            ['C', 'D', 'M'],
            ['M']
        ]
        result = ''
        i = 0
        while num:
            roman = roman_list[i]
            num_ = num%10
            if num_ <= 3:
                result = roman[0]*num_ + result
            elif num_ == 4:
                result = roman[0] + roman[1] + result
            elif num_ == 5:
                result = roman[1] + result

            elif 5 < num_ <= 8:
                result = roman[1] + roman[0]*(num_-5) + result

            elif num_ == 9:
                result = roman[0] + roman[2] + result

            i += 1
            num = num // 10
        return result