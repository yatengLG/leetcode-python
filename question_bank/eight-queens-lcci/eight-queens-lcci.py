# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了88.57% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了22.64% 的用户

解题思路：
    回溯
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_record = []     # 列记录
        dia1_record = []    # 对角线1记录
        dia2_record = []    # 对角线2记录
        result = []
        def backtrack(r, current):
            if r >= n:  # 如果最后一行也放置完成，则添加到最终结果中
                board = [['.' for _ in range(n)] for _ in range(n)]
                for r,c in current:
                    board[r][c] = 'Q'
                    board[r] = ''.join(board[r])
                result.append(board[:])
                return
            for c in range(n):  # 在本行中依次在每一列上进行放置
                if c not in col_record and r-c not in dia1_record and r+c not in dia2_record:   # 查看是否已经放置过
                    col_record.append(c)
                    dia1_record.append(r-c)
                    dia2_record.append(r+c)
                    backtrack(r+1, current+[(r, c)])    # 放置下一行
                    col_record.pop()
                    dia1_record.pop()
                    dia2_record.pop()
        backtrack(0, [])
        return result