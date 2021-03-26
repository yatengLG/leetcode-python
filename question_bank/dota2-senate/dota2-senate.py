# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了56.10% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了25.77% 的用户

解题思路：
    模拟
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)   # 将字符串转换为列表，便于操作
        start = senate[0]   # 当前哪个阵营行使权利
        start_n = 0 # 统计当前行使权利的行使权数
        while len(set(senate)) != 1:    # 当议院只剩一个阵营时跳出
            i = 0   # 列表索引
            while i < len(senate):
                if senate[i] == start:  # 如果当前议员属于行使权利的阵营，则当前阵营行使权+1，处理下一个议员
                    start_n += 1
                    i += 1
                else:   # 如果当前议员属于行使权利阵营的对立阵营，则行使权利的阵营禁止该议员，行使权利的阵营行使权-1
                    del senate[i]   # 删除该议员
                    start_n -= 1    # 行使权-1
                    if start_n < 1: # 若行使权==0，则 行使权利的阵营转变
                        start = senate[i] if i < len(senate) else senate[0]
                        start_n = 0
        return 'Radiant' if senate[0]=='R' else 'Dire'
