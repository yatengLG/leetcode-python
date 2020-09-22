# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了88.95% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了48.64% 的用户

解题思路：
    按照题意，模拟数字加1
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1 # 先要加的1，以及记录进位
        index = len(digits)-1
        while index > -1:   # 从最后一位开始计算
            num = digits[index] + add   # 当前位加上进位
            add = num//10       # 更新进位
            digits[index] = num % 10    # 更新当前值
            index -= 1  # 处理下一个
        if add > 0:
            digits.insert(0, add)   # 如果最终进位不为0，则在最开始添加一位
        return digits