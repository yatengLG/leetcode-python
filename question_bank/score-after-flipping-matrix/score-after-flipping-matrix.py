# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了98.48% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了6.28% 的用户

解题思路：
    现将对行进行翻转，将每行第一个变为1
    其次，对列进行变换，如果本列0数量较多，则翻转
"""
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):  # 按行，如果每行第一个为0，则翻转该行
            if A[i][0] == 0:
                A[i] = [1 if a == 0 else 0 for a in A[i]]

        for j in range(n):  # 按列
            sum_ = 0
            for i in range(m):
                sum_ += A[i][j] # 统计本行非0值
            if sum_ < m/2:  # 如果非0值少，则翻转该列
                for i in range(m):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        result = 0
        for a in A:
            result += int('0b'+''.join([str(aa) for aa in a]), base=2)
        return result