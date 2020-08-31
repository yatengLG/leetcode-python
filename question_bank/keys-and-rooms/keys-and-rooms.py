# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：80 ms, 在所有 Python3 提交中击败了87.03% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了10.98% 的用户

解题思路：
    深度优先遍历，递归
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        record = set()
        def visit_room(key):
            record.add(key)
            now_keys = rooms[key]
            for key in now_keys:
                if key not in record:
                    visit_room(key)

        visit_room(0)
        if len(record) == len(rooms):
            return True
        else:
            return False