# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了98.07% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了74.27% 的用户

解题思路：
    [h, k] 表示，其中 h 是这个人的身高，k 是应该排在这个人前面且身高大于或等于 h 的人数

        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    先进行排序，按照h从高到低，k从小到大排列
        [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    然后依次插入结果即可
    后插入的必定比先插入的个子低，所以，此时按照k插入即可
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1])) # 按个头从高到低，前面人数从少到多排序
        result = []
        for p in people:
            result.insert(p[1], p)  # 依次按照前面高个子数量插入列表
        return result