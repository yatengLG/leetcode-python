# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：76 ms, 在所有 Python3 提交中击败了57.29% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了5.05% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = []    # 用于保存 不能放置的行，代表此行已有Q，已被使用
        col = []    # 不能放置的列
        obl1 = []   # 不能放置的斜行1
        obl2 = []   # 不能放置的斜行2
        result = [] # 最终结果，保存棋子的存放处
        def solve(r, current):  # 当前行r, 当前已经放置的棋子
            if r == n:          # 如果已经到最后一行，则添加到最终结果中
                result.append(current.copy())
            for j in range(n):  # 遍历列
                if r not in row and j not in col and r-j not in obl1 and r+j not in obl2:   # 放置位置验证
                    row.append(r)   # 放置棋子后，将当前行添加到已使用列表中
                    col.append(j)
                    obl1.append(r-j)
                    obl2.append(r+j)
                    current.append((r,j))   # 添加到当前放置棋子列表中
                    solve(r+1, current)     # 开始下一行

                    row.pop()   # 回溯
                    col.pop()
                    obl1.pop()
                    obl2.pop()
                    current.pop()

        solve(0, [])    # 从第一行开始

        # 将棋子坐标转换到棋盘
        board = [[['.' for _ in range(n)] for _ in range(n)] for _ in range(len(result))]
        for n, rc in enumerate(result):
            for r, c in rc:
                board[n][r][c] = 'Q'
                board[n][r] = ''.join(board[n][r])

        return board