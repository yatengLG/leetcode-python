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


"""
执行用时：52 ms, 在所有 Python3 提交中击败了16.03% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了47.18% 的用户

解题思路：
    例： n = 4
    
            0   0   0   0   0000
                        1   0001
                    1   1   0011
                        0   0010
                1   1   0   0110
                        1   0111
                    0   1   0101
                        0   0100
            1   1   0   0   1100
                        1   1101
                    1   1   1111
                        0   1110
                0   1   0   1010
                        1   1011
                    0   1   1001
                        0   1000
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        strings = []
        for i in range(n):
            string=''
            reverse = False
            while len(string) < (2**n):
                if reverse:
                    string += '1' * int(2 ** i) + '0' * int(2 ** i)
                else:
                    string += '0' * int(2 ** i) + '1' * int(2 ** i)
                reverse = not reverse
            strings.append(string)

        result = [0 for _ in range(2**n)]
        for j, string in enumerate(strings):
            for i, s in enumerate(string):
                result[i] += int(s) * (2 ** j)
        return result
