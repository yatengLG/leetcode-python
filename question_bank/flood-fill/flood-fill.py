# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：92 ms, 在所有 Python3 提交中击败了79.49% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了92.11% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        directions  = [[-1, 0], [1, 0], [0, -1], [0, 1]]    # 上下左右的四个偏移量
        oldColor = image[sr][sc]    # 先查看起始点的颜色
        rc_list = [[sr, sc]]    # 用于记录需要渲染的点的坐标

        if newColor == oldColor:    # 如果新旧颜色相同，直接返回
            return image

        while rc_list:      # 循环处理需要渲染的颜色
            sr, sc = rc_list.pop()  # 出列表

            image[sr][sc] = newColor    # 更改颜色

            for direction in directions:    # 计算上下左右四个点
                nr, nc = sr+direction[0], sc+direction[1]

                if 0 <= nr < r and 0 <= nc < c: # 判断是否越界
                    if image[nr][nc] == oldColor:   # 判断是否为需要渲染的点
                        rc_list.append([nr, nc])    # 进列表

        return image