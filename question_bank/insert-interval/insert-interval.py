# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了93.88% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了10.79% 的用户

解题思路：
    模拟插入
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        start, end = newInterval[0], newInterval[1]
        if intervals == []: # 如果起始列表为空，则直接返回待插入列表
            return [newInterval]
        while i < len(intervals):
            if intervals[i][1] < start: # 待插入列表在当前列表元素右侧
                result.append(intervals[i]) # 直接插入当前元素
            elif end < intervals[i][0]: # 待插入列表在当前列表元素左侧，将待插入列表插入结果，以当前列表值更新待插入列表
                result.append([start, end])
                start, end = intervals[i]
            else:   # 当前列表与待插入列表存在交集，则更新待插入列表
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            i += 1
        result.append([start, end]) # 最后将待插入列表插入最终结果
        return result