# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：180 ms, 在所有 Python3 提交中击败了5.52% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.06% 的用户

解题思路：
    回溯
    回溯，直到找到一个满足条件的值
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        def backtrack(start:list, current:list):
            if len(current) >= 2**n:
                for b in current:
                    num = 0
                    for i, v in enumerate(b[::-1]):
                        num += v*2**i
                    result.append(num)
                return True

            for i in range(n):
                start_copy = start[:]
                start_copy[i] = 0 if start_copy[i]==1 else 1
                if start_copy not in current:
                    current.append(start_copy)
                    if backtrack(start_copy, current):
                        return True
                    current.pop()
        if backtrack([0]*n,[[0]*n]):
            return result
        else:
            return []



