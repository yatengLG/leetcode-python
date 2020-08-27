# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了95.23% 的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了36.92% 的用户

解题思路：
    回溯
    具体见代码注释
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict # 由于存在有的节点没有指向的情况，需要给终点一个默认值
        records = defaultdict(list) # 字典，用于存储 当前节点可以通向的节点 {from :[to_1, to_2, to_3, ...]}
        for ticket in tickets:
            if ticket[0] not in records:
                records[ticket[0]] = [ticket[1]]
            else:
                records[ticket[0]].append(ticket[1])
                records[ticket[0]].sort()   # 为了方便处理，对通向的节点进行一个排序

        result = ['JFK']    # result保存最终的路径，其实点为'jfk'
        def find(start):    # 回溯
            if len(result) == len(tickets)+1:   # 如果路径都走过了，则返回true  。result包含路径与起始点.
                return True
            tos = records[start]    # 当前节点 可通向的节点
            for to in tos:
                to = tos.pop(0)     # 取出一个节点，加入最终路径result中
                result.append(to)
                if find(to):        # 以当前节点继续走，如果当前节点符合最终路径要求，return
                    return True
                result.pop()        # 当前节点继续走，不符合最终路径要求，回溯，将当前节点从最终路径中删除
                records[start].append(to)   # 将当前节点存回 字典中
            return False

        find(start='JFK')
        return result