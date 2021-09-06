# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.10% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了92.43% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        S = list(S)
        count = collections.defaultdict(int)    # 用于记录每个字符出现的次数
        for s in S:
            count[s] += 1
        if max(count.values()) > (len(S) + 1) / 2:  # 若有一个字符出现的次数大于总体长度的一半， 返回‘’
            return ''
        keys = list(count.keys())   # 出现的字符
        keys.sort(key=lambda x: count[x], reverse=True) # 对出现的字符以出现次数排序，从多到少
        ss = [k for k in keys for _ in range(count[k])] # 以字符出现次数，复制字符(这里直接对元数据S排序会出错，有的字符出现次数相同)
        # 以出现次数从多到少，依次将字符间隔地填入结果中
        start = 0
        step = 0
        for s in ss:
            if start + step * 2 > len(S)-1:
                start += 1
                step = 0
            S[start + step * 2] = s
            step += 1
        return ''.join(S)