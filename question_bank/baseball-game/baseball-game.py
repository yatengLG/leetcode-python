# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了88.49% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了42.15% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for op in ops:
            if op == '+':
                record.append(sum(record[-2:])) # 前两轮得分和
            elif op == 'D':
                record.append(record[-1] * 2)   # 前一轮得分的2倍
            elif op == 'C':
                record.pop()    # 前一轮得分无效，剔除
            else:
                record.append(int(op))  # 录入得分
        return sum(record)