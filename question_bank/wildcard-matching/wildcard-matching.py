# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：832 ms, 在所有 Python3 提交中击败了71.51% 的用户
内存消耗：22.5 MB, 在所有 Python3 提交中击败了21.67% 的用户

解题思路：
    动态规划

    使用dp[i][j] 表示，p[i]之前部分与s[j]之前部分是否匹配
    例：
            ''  a   d   c   e   b
        ''  T   F   F   F   F   F
        *   T
        a   F
        *   F
        b   F

        表中，第一行第一类为空字符串，
        对于s中的空字符串，只有*或者''可以匹配。  当*时，dp[i][0] = dp[i-1][0]
        p中'' 只可以匹配''。则 dp[0][j] = False     j!=0


            ''  a   d   c   e   b
        ''  T   F   F   F   F   F
        *   T   T   T   T   T   T
        a   F   T   F   F   F   F
        *   F   T   T   T   T   T
        b   F   F   F   F   F   T

        对于表中其他位置，存在三种情况:
            1. p[i] == '*', 可以匹配一切，包含空字符串，
                则匹配空字符串时：dp[i][j] == dp[i-1][j]
                匹配1或多个字符时：  dp[i][j] == dp[i][j-1]
            2. p[i] == '?', 可匹配单个字符
                dp[i][j] == dp[i-1][j-1]
            3. 其他字符时，
                dp[i][j] == p[i]=s[j] and dp[i-1][j-1]
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_s = len(s)
        l_p = len(p)

        dp = [[False for _ in range(l_s+1)] for _ in range(l_p+1)]

        dp[0][0] = True
        for i in range(l_p):
            if p[i] == '*':
                dp[i+1][0] = dp[i][0]


        for i in range(l_p):
            for j in range(l_s):
                if p[i] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
                elif p[i] == '?' and s[j] != '':
                    dp[i+1][j+1] = dp[i][j]
                elif p[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]