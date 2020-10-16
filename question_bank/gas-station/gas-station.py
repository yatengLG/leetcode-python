# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了89.07% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了5.02% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = [g-c for g, c in zip(gas, cost)]  # 计算当前站点到下个站点的净消耗
        if sum(surplus) < 0:    # 如果 整体净消耗 < 0, 则不可能成环
            return -1
        # 当净消耗>=0时，必然可以成环，但是需要考虑从哪里作为开始
        g = 0
        start = 0   # 以0为起始点
        for i, sur in enumerate(surplus):
            g += sur    # 当前加油站净消耗
            if g < 0:   # 如果到当前加油站净消耗<0， 则[:i]部分的净消耗和小于0。前面不可能成环
                g = 0   # 将净消耗归0, 从下一个加油站开始作为起始点
                start = i+1
        return start