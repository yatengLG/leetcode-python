# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：3020 ms, 在所有 Python3 提交中击败了5.04% 的用户
内存消耗：33 MB, 在所有 Python3 提交中击败了32.54% 的用户

解题思路：
    动态规划
    题中需要r*y*r*格式，由r*、r*y*、r*y*r*一步一步满足

        r   r   r   y   y   y   r   r   y   y   y   r   r
        0   0   0   1   2   3   3   3   4   5   6   6   6   # r*
            1   1   0   0   0   1   2   2   2   2   3   4   # r*y*
                1   2   1   1   0   0   1   2   3   2   2   # r*y*r*

        y   r   y   y   r   y
        1   1   2   3   3   4   # r*
            2   1   1   2   2   # r*y*
                3   2   1   2   # r*y*r*

"""
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        dp = [[ float('inf') for _ in range(3)]  for _ in leaves]
        dp[0][0] = int(leaves[0]!='r')
        for i in range(1, len(leaves)):
            dp[i][0] = dp[i-1][0] + int(leaves[i]!='r')                     # r* 只依赖于 r*情况
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(leaves[i]!='y')    # r*y* 可由 r*+y 和r*y*+y 得到，依赖于 r* 和r*y*情况
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + int(leaves[i]!='r')    # r*y*r* 可由 r*y*+r 和 r*y*r*+r 得到，依赖于r*y* 和 r*y*r*情况
        return dp[-1][2]