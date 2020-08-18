# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了72.15% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了62.55% 的用户

解题思路：
    自顶向下叠加
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            m = len(triangle[i])
            for j in range(m):
                if j-1 < 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j+1 > m-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        return min(triangle[-1])


"""
执行用时：44 ms, 在所有 Python3 提交中击败了88.51% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了30.46% 的用户

解题思路：
    自底向上，省去了边界判断以及最后的找最小值
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n-1, 0, -1):
            for j in range(i):  # 第n行有n-1个元素，
                triangle[i-1][j] = min(triangle[i][j], triangle[i][j+1]) + triangle[i-1][j] # 上一行的元素等于 上一行元素+ 本行相邻元素的最小值
        return triangle[0][0]