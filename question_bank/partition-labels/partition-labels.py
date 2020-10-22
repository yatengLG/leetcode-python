# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.21% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.01% 的用户

解题思路:
    具体实现见代码注释
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        record = {}
        for i in range(len(S)-1, -1, -1):   # 先遍历字符串，统计各字符出现的最后位置
            if S[i] not in record:
                record[S[i]] = i

        result =[]
        start, end = 0, 0   # 当前划分区间的 起始与结束
        for i, c in enumerate(S):
            end = max(end, record[c])   # 当前区间的结束 以当前区间字符的最后位置为准
            if i == end:    # 如遍历到当前区间内字符的最后位置，则当前区间为一个可划分区间
                result.append(end-start+1)
                start = i+1 # 划分区间后，下次划分的其实start需要移动
        return result