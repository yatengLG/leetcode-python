# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了74.47% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了7.95% 的用户

解题思路：
    只能向右或向下前进。
    则当前格的路径数等于左侧格的路径数+上侧格的路径数
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    例子：
        1   1   1   1   1   1
        1   2   3   4   5   6
        1   3   6   10  15  21
        1   4   10  20  35  56
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
