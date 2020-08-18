# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了94.07% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了85.98% 的用户

解题思路：
    本题分以下几种情况：
        1. ""                       # 0
        2. "_" 1 ~ 9                # 1
        3. 'x10'                    # dp[i-2]
        4. 'x1_' x11 ~ x19          # dp[i-1] + dp[i-2]
        5. 'x20'                    # dp[i-2]
        6. 'x2_' x21 ~ x26          # dp[i-1] + dp[i-2]
        7. 'x2_' x27 ~ x29          # dp[i-1]
        8. 'x3_' x31 ~ x39          # dp[i-1]
        9. 'x30'                    # 0
       11. 'x00'                    # 0
       10. 'x0_' x01 ~ x09          # dp[i-1]
    分别处理即可
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0 or s[0] == '0':
            return 0

        dp = [[] for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n == 1:
            return dp[1]

        for i in range(1, n):
            if s[i-1] == '0':   # 0_
                if s[i] == '0':     # x00
                    return 0
                else:               # x01 x02 x03 ~ x09
                    dp[i+1] = dp[i+1-1]
            elif s[i-1] == '1':     # x1_
                if s[i] == '0':     # x10
                    dp[i+1] = dp[i+1-2]
                else:               # x11 ~ x19
                    dp[i+1] = dp[i+1-1] + dp[i+1-2]
            elif s[i-1] == '2':     # x2_
                if s[i] == '0':  # x20
                    dp[i+1] = dp[i+1-2]
                elif s[i] in '789': # x27 ~ x29
                    dp[i+1] = dp[i+1-1]
                else:               # x21 ~ x26
                    dp[i+1] = dp[i+1-1] + dp[i+1-2]
            else:                   # x3_ ~ x9~
                if s[i] == '0':
                    return 0
                else:
                    dp[i+1] = dp[i+1-1]
        return dp[-1]