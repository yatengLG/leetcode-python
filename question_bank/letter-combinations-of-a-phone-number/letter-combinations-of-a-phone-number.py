# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了86.65% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了86.43% 的用户

解题思路：
    多重循环，依次填入字符
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            '1':[],
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }

        if digits == '':
            return []

        result = letter_dict[digits[0]]
        if len(digits) == 1:
            return result

        for s in digits[1:]:
            result_ = []
            for letter in letter_dict[s]:
                for r in result:
                    result_.append(r+letter)
            result = result_.copy()

        return result