# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：84 ms, 在所有 Python3 提交中击败了93.21% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了27.86% 的用户

解题思想：

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_ = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_ = max(dp[i][0], max_)

        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])
            max_ = max(dp[0][j], max_)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0

                max_ = max(dp[i][j], max_)
        return max_**2


"""
执行用时：120 ms, 在所有 Python3 提交中击败了30.10% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了61.68% 的用户

解题思路：
    整理代码后，效率变低，但是逻辑上更顺畅
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_ = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i+1-1][j+1-1], dp[i+1][j+1-1], dp[i+1-1][j+1]) + 1
                else:
                    dp[i+1][j+1] = 0

                max_ = max(dp[i+1][j+1], max_)
        return max_**2