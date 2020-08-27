# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了92.93% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了23.45% 的用户

解题思路：
    某一数值num的比特位为1的计数，等于其 /2的余数为1 的数量
    例：
            13  余                  6   余
        /2  6   1               /2  3   0
        /2  3   0               /2  1   1
        /2  1   1               /2  0   1
        /2  0   1

"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            dp[i] = dp[i // 2] if i%2 == 0 else dp[i // 2]+1
        return dp