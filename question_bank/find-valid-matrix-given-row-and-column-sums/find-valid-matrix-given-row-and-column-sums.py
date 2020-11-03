# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了90.00% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了13.51% 的用户

解题思路：
    贪心算法
    在每个空缺处，填可以填的最大值
    在每个空缺处填入行列和中的最小值，则填完后，必然会有行列和中的某一值为0，可以直接跳过该行/列，提高效率
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        result = [[0 for _ in range(c)] for _ in range(r)]
        i, j = 0, 0
        while i < r and j < c:
            val = min(rowSum[i], colSum[j]) # 取当前空位对应行列值的最小值，填入该空位
            result[i][j] = val

            rowSum[i] -= val    # 因为填的是当前行列中最小的那个，则每次填完，则必有行列之一的和为0，直接跳过当前行列即可
            if rowSum[i] == 0:
                i += 1

            colSum[j] -= val
            if colSum[j] == 0:
                j += 1

        return result


"""
执行用时：324 ms, 在所有 Python3 提交中击败了74.59% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了17.57% 的用户

解题思路：
    贪心算法
    在每个空缺处，填可以填的最大值
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        result = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                val = min(rowSum[i], colSum[j]) # 取当前空位对应行列值的最小值，填入该空位
                result[i][j] = val
                rowSum[i] -= val    # 更新当前行列的和的值
                colSum[j] -= val
        return result