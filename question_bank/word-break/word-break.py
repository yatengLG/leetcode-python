# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了45.63% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了86.84% 的用户

解题思路：
    总体的思路是合成，通过两个都匹配的子串，来证明合成的串 可拆分
    依次判断子串是否可以拆分, 双指针依次遍历。若s[:i] and s[i:j] 都可以拆分，则s[0：j]可以拆分

    '' l e e t c o d e
    T  F F F T F F F T
    i
       j
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

"""
执行用时：44 ms, 在所有 Python3 提交中击败了90.36% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了65.15% 的用户

解题思路：
    这个是参考leetcode他人提出的思路
    与上例不同在于，上例主要思想是合成，先找到一个匹配的子串，然后向后匹配，再找一个子串，然后合成的子串可拆分 s[:i]+s[i:j] = s[:j]
    遍历一个子串，然后去查看该子串是否可以拆分，若可拆分，则s[:j] + s[j:i] == s[i] 当前子串可拆分
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False for _ in range(n+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]