# -*- coding: utf-8 -*-
# @Author  : LG


"""
执行用时：196 ms
内存消耗：15.6 MB
解题思路：
    将所有的点存在一个列表里。
    对列表按距离进行排序。
    最简洁，但也最慢。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        lists = [[r, c] for r in range(R) for c in range(C)]
        lists = sorted(lists, key=lambda p: abs(p[0]-r0)+abs(p[1]-c0))
        return lists


"""
执行用时：180 ms, 在所有 Python3 提交中击败了72.17% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了100.00% 的用户
解题思路：
    循环计算各点与原点距离，存入一个列表中，将同距离点都存在一个列表中，列表第一个元素中存储距离为1的点，第二个元素中存储距离为2的点。
    遍历列表，获取点。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        dists = [[] for _ in range(R+C)]
        for r in range(abs(R)):
            for c in range(abs(C)):
                dists[abs(r-r0)+abs(c-c0)].append([r, c])

        result = []
        for dist in dists:
            if dist !=[]:
                result.extend(dist)
        return result


"""
执行用时：172 ms
内存消耗：15.3 MB
解题思路：
    思路与2相同，但将列表换成字段。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        dists = {}
        for r in range(abs(R)):
            for c in range(abs(C)):
                dist = abs(r-r0)+abs(c-c0)
                if dist not in dists.keys():
                    dists[dist] = []
                dists[dist].append([r, c])
        result = []
        dists_keys = sorted(dists.keys())
        for dist in dists_keys:
            result.extend(dists[dist])
        return result