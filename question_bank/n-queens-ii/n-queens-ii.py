# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了80.87% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了8.27% 的用户

解题思路：
    回溯
    同N皇后解题思路，但由于只需要计算题解数量
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = []
        obl1 = []
        obl2 = []
        result = [0]

        def backtrack(i:int, current:int):
            if current == n:
                result[0] += 1
                return

            for j in range(n):
                if j not in col and j-i not in obl1 and j+i not in obl2:
                    col.append(j)
                    obl1.append(j-i)
                    obl2.append(j+i)
                    current += 1
                    backtrack(i+1, current)
                    current -= 1
                    col.pop()
                    obl1.pop()
                    obl2.pop()

        backtrack(0, 0)
        return result[0]