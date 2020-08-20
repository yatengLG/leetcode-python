# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：128 ms, 在所有 Python3 提交中击败了92.83% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了29.48% 的用户

解题思路：
    动态规划
    计算 左上角到某一点的 和

    计算两点之间的和时， 等于右下角点到原点的和 - 上侧 - 左侧 + 左上角到原点的和
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix and matrix[0]:
            self.m = len(matrix)
            self.n = len(matrix[0])

            self.dp = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]

            for i in range(1, self.m+1):
                for j in range(1, self.n+1):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return 0
        # print(self.dp)
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        # print(self.dp[row2][col2], self.dp[row1-1][col1], self.dp[row1][col1-1], self.dp[row1-1][col1-1])
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
