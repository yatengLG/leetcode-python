# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：216 ms, 在所有 Python3 提交中击败了47.71% 的用户
内存消耗：31.7 MB, 在所有 Python3 提交中击败了5.07% 的用户

解题思路：
    动态规划

    例：
            ''  h   o   r   s   e
        ''  0   1   2   3   4   5
        r   1   1   2   2   3   4
        o   2   2   1   2   3   4
        s   3   3   2   2   2   3

        当 world2[i] == world1[j]时， dp[i][j] = dp[i-1][j-1]
        当 world2[i] != world1[j]时，
            1. dp[i][j] = dp[i-1][j]+1      可通过world2[i-1] 删除一个元素得到 world1[j]
            2. dp[i][j] = dp[i-1][j-1]+1    可通过world2[i]， world1[j] 替换最后一个元素得到
            3. dp[i][j] = dp[i][j-1]+1      可通过world2[i] 插入一个元素得到 world1[j-1]，
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[[] for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        dp[0] = list(range(m+1))

        for i in range(n):
            for j in range(m):
                if word2[i] == word1[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
        return dp[-1][-1]