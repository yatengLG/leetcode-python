# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.17% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了75.98% 的用户

解题思路：
    动态规划
    由于网格中加入了障碍
    障碍右侧的网格路径数，只依赖于网格上侧
    障碍下侧的网格路径数，只依赖于网格左侧
    为统一思路，将存在障碍的网格路径数置为0 即可
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0

        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]