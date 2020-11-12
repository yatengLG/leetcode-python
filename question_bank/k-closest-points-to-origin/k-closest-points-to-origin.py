# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：688 ms, 在所有 Python3 提交中击败了97.75% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了33.70% 的用户

解题思路：
    以到原点的距离排序，然后取前K个即可
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0]**2+point[1]**2)
        return points[:K]