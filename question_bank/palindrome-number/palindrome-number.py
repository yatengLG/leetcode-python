# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了38.64% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了11.30% 的用户

解题思路：
    这里没有将数字转字符串进行判断。
    而是首先对数字进行了判断，限制在一个范围内，然后将数字翻转后进行判断。
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x>2147447412: # 2147447412 是 2*31-1 内最大的回文数。负数 按题意可知均不回文
            return False
        x_copy = x
        num = 0
        while x:                # 翻转数字
            num = num*10 + x%10
            x = x//10
        if num == x_copy:
            return True
        else:
            return False