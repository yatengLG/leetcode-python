# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了96.66% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了76.81% 的用户

解题思路：
    先将字符串按空格划分， 然后把每部分翻转，然后在每部分中间添加空格构成字符串
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')   # 以空格划分
        for i in range(len(ss)):
            ss[i] = ss[i][::-1] # 翻转每一部分
        return ' '.join(ss) # 添加空格