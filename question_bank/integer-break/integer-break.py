# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了97.80% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了63.31% 的用户

解题思路：
    动态规划
    例：
        2   1   1
        3   2   1
        4   2   2
        5   3   2
        6   3   3
        7   3   2   2
        8   3   3   2
        9   3   3   3
        10  3   3   2   2
        11  3   3   3   2
        12  3   3   3   3
    可看出，dp[i]=dp[i-3]*3  i>6
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[2:7] = [1,2,4,6,9]
        for i in range(7,n+1):
            dp[i] = dp[i-3] *3
        return dp[n]