# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了95.42% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    列表中指定下标求和。
    因为是环形，只需计算被起点与终点分割成的俩部分长度即可。
    对于 start > destination 的情况，进行处理
"""

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dist1 = sum(distance[start: destination])
        dist2 = sum(distance[0: start]) + sum(distance[destination:])
        return min(dist1, dist2)