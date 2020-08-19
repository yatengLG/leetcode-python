# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：164 ms, 在所有 Python3 提交中击败了77.50% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了91.44% 的用户

解题思路：
    三指针，参考的官方解题思路：https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode/
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            min_ = min(2*dp[p2], 3*dp[p3], 5*dp[p5])
            dp[i] = min_
            if dp[p2] * 2 == min_:
                p2 += 1
            if dp[p3] * 3 == min_:
                p3 += 1
            if dp[p5] * 5 == min_:
                p5 += 1
        return dp[-1]