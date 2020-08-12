# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了35.61% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了33.84% 的用户

解题思路：
    拿第一个字符串去比较其他字符串
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        for string in strs[1:]:
            result_ = ''
            for r,s in zip(result, string):
                if r == s:
                    result_ += r
                else:
                    break
            result = result_

            if result == '':
                break
        return result