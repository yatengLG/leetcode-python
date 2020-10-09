# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.80% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了72.55%

解题思路：
    先遍历宝石类别，
    然后遍历石头，统计各宝石数量
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_dic = {}  # 各宝石数量
        for j in J:
            jewel_dic[j] = 0    # 遍历宝石类别，各宝石数量起始为0

        for s in S: # 遍历石头
            if s in jewel_dic:  # 对应宝石数量+1
                jewel_dic[s] += 1
        return sum(jewel_dic.values())