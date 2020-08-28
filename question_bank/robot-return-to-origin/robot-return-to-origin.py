# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：196 ms, 在所有 Python3 提交中击败了5.21% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了86.94% 的用户

解题思路：
    模拟机器人运动
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = {'U': [0, 1], # 运动方向对应的坐标运动
               'D': [0, -1],
               'L': [-1, 0],
               'R': [1, 0]}
        start = [0, 0]  # 起始点
        for move in moves:      # 开始运动
            start = [i+j for i,j in zip(start, dic[move])]  # 每次运动后的坐标
        if start == [0, 0]: # 判断是否回到原点
            return True
        return False


"""
执行用时：40 ms, 在所有 Python3 提交中击败了96.39% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了69.83% 的用户

解题思路：
    直接统计给定字符串中，各方向移动的次数
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D')
