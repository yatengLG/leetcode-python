# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.83% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了91.78% 的用户

解题思路：
    动态规划
    寻找连续重复多次但不重叠的子数组
    例：
        arr = [1,2,1,2,1,1,1,3], m = 2, k = 2

        1   2   1   2   1   1   1   3
        i-m     i       i+m
        0   0   1   1   0   0   0   0

        从m开始遍历
        若arr[i-m:i] == arr[i:i+m]则子数组相同，
            dp[i] = dp[i-m]
    具体实现见代码注释
"""
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)    # 数组长度
        dp = [0 for _ in range(n)]

        for i in range(m, n-m):   # 从m开始遍历,
            if arr[i-m: i] == arr[i:m+i]:   # 若当前其实字符m长度数组与 当前字符前m个字符组成的数组相等
                dp[i] = dp[i-m] + 1

        if max(dp)+1 >= k:
            return True
        else:
            return False
