# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了67.68% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.70% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = [int(s) for s in str(N)]    # 转换为列表，便于计算
        i = len(N) - 1
        while i > 0:    # 从后往前比较
            if N[i] < N[i-1]:   # 如果当前元素比前一个元素小
                N[i:] = [9] * (len(N) - i)  # 则将当前元素后部分均置为9， 前一个元素-1
                N[i-1] = N[i-1] - 1
            i-=1
        return int(''.join([str(n) for n in N]))