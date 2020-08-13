# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了95.41% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了47.58% 的用户

解题思路：
    动态规划
    每次只能爬1层 或 爬2层。
    例：5层， 可以由3层 +2 到达、也可以4层+1 到达。
    所以5层的方法数 = 3层的方法数 + 4层的方法数
    dp[i] = dp[i-1] + dp[i-2]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [[] for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]