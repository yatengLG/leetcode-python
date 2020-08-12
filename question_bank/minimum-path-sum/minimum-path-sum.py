# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了99.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了8.33% 的用户

解题思路：
    计算每个点 上侧与左侧的最小值，作为当前点到左上点的最短距离。
    依次计算，直到遍历完整个路径矩阵
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        for i in range(n):
            if i >0:
                grid[i][0] = grid[i-1][0] + grid[i][0]
            else:
                grid[i][0] = 0 + grid[i][0]

        for j in range(1, m):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        if m > 1:
            for i in range(1, n):
                if n >1:
                    for j in range(1, m):
                        grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[n-1][m-1]


