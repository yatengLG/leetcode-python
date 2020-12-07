# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了93.78% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了56.53% 的用户

解题思路：
    模拟杨辉三角的生成过程
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):   # 每一行有i个数
            row = [1]   # 第一个数是1
            for j in range(1, i-1): # 从第二个到倒数第二个起，等于上一行对应数的和
                row.append(result[-1][j-1] + result[-1][j])
            if i > 1:
                row.append(1)
            result.append(row)
        return result