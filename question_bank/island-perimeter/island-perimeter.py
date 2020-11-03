# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：152 ms, 在所有 Python3 提交中击败了68.28% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了58.86% 的用户

解题思路：
    每存在一个相邻岛屿，则边各少一条。
    具体实现见代码注释
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num = 0 # 记录岛屿数
        neighbor = 0    # 记录相邻岛屿数
        m, n = len(grid), len(grid[0])  #
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # 找到岛屿
                    num += 1    # 岛屿数+1
                    if 0 <= i-1 and grid[i-1][j] == 1:  # 查看岛屿四周，找相邻岛屿
                        neighbor += 1   # 存在相邻岛屿，相邻岛屿数+1
                    if i+1 < m and grid[i+1][j] == 1:
                        neighbor += 1
                    if 0 <= j-1 and grid[i][j-1] == 1:
                        neighbor += 1
                    if j+1 < n and grid[i][j+1] == 1:
                        neighbor += 1
        return num*4-neighbor