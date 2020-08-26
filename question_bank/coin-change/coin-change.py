# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1668 ms, 在所有 Python3 提交中击败了45.86% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了67.60% 的用户

解题思路：

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            record = []
            for coin in coins:
                if i - coin == 0:
                    dp[i] = 1
                    break
                if i - coin > 0 and dp[i-coin] >= 0:
                    record.append(dp[i-coin])
            if record != [] and dp[i] != 1:
                dp[i] = min(record) + 1
        return dp[-1]


"""
执行用时：1556 ms, 在所有 Python3 提交中击败了62.00% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了28.90% 的用户

解题思路：
    精简下代码,并将两次循环的顺序调换了下，第二次循环从当前硬币币值开始
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1