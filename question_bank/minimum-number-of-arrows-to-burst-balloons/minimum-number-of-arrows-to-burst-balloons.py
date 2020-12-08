# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：128 ms, 在所有 Python3 提交中击败了29.39% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了52.88% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort()
        result = 1
        now = points[0]
        i = 0

        while i < len(points):
            # print(points, now, points[i])
            if now[1] >= points[i][0]:  # 有交叉
                now = [max(now[0], points[i][0]), min(now[1], points[i][1])]    # 更新箭的范围
                i += 1
            else:
                now = points[i]
                i += 1
                result += 1
        return result
