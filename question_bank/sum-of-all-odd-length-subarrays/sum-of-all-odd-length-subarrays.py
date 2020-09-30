# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：72 ms, 在所有 Python3 提交中击败了56.70% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了25.43% 的用户

解题思路：
    先以奇数长度截取字符串，求和
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = []
        n = len(arr)

        for l in range(1, n+1): # 依次尝试 1~n的长度
            if l%2 == 1:    # 如果当前 长度为奇数
                for j in range(n-l+1):  # 以当前长度截取字符串，求和
                    result.append(sum(arr[j:j+l]))
        return sum(result)

"""
执行用时：72 ms, 在所有 Python3 提交中击败了56.70% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了84.07% 的用户

解题思路：
    先以奇数长度截取字符串，求和
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = []
        n = len(arr)

        for l in range(1, n+1, 2): # 依次尝试 1~n的长度
            for j in range(n-l+1):  # 以当前长度截取字符串，求和
                result.append(sum(arr[j:j+l]))
        return sum(result)
