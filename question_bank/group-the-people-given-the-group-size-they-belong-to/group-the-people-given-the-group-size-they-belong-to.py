# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了95.78% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了7.85% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        dp = [[] for _ in range(len(groupSizes)+1)] # 每种用户组的用户列表
        for i, group in enumerate(groupSizes):
            dp[group] += [i]    # 将用户下标存入对应的用户组
            if len(dp[group]) == group: # 如果当前用户组的用户数等于指定数
                result.append(dp[group][:]) # 添加到最终结果
                dp[group] = []  # 重置对应的用户组
        return result