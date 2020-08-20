# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：248 ms, 在所有 Python3 提交中击败了36.27% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了10.36% 的用户

解题思路：
    模拟点击
    当发生点击操作时，有三种情况：
        1. 点击到'M'， 也就是点击到雷，此时，把雷 改成'X'， 返回即可
        2. 点击到'E'，也即是未点到雷时，需要遍历周围情况：
            3. 是否与雷相邻，，如果相邻，则把当前'E'， 改成周围雷的数量
            4. 如果不相邻，则改为'B'，且开始遍历周围其他块
    具体实现见代码备注
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1] ]    # 八个方位

        def f(i, j):    # 定义一个点击函数，用于遍历
            record = [] # 记录周围需要点击的'E'的坐标
            mines = 0   # 记录当前坐标周围雷的数量
            for direction in directions:    # 八个方位，挨着遍历
                new_i, new_j = i + direction[0], j+direction[1]
                if 0 <= new_i < m and 0 <= new_j < n:   # 如果越界，则忽略
                    if board[new_i][new_j] == 'M':      # 周围有雷， 雷数量+1
                        mines += 1
                    elif board[new_i][new_j] == 'E':    # 周围不是雷，将这个坐标记录下来
                        record.append([new_i, new_j])

            if mines == 0:  # 如果雷的数量是0，则为'B', 且需要遍历周围其他不是雷的区域
                board[i][j] = 'B'
                for new_i, new_j in record: # 遍历周围其他区域
                    f(new_i, new_j)
            else:
                board[i][j] = str(mines)    # 如果存在雷，则将该坐标 改为雷的数量

        i, j = click
        if board[i][j] == 'M':  # 第一次点击，是雷，则需要改为X，返回即可
            board[i][j] = 'X'
            return board

        elif board[i][j] == 'E':    # 不是雷，则需要以当前坐标为中心开始遍历周围点
            f(i, j)

        return board