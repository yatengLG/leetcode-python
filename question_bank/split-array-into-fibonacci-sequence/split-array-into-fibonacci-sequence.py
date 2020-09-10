# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：148 ms, 在所有 Python3 提交中击败了35.57% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了36.81% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def backtrack(S, current):
            if S == '' and len(current) > 2:    # 字符串均处理完，且当前序列长度大于2， 返回最终结果
                return True

            if S == '': # 当字符串处理完时，跳出
                return

            for i in range(1, len(S)+1): # 遍历当前字符串
                if (S[0] == '0' and i == 1) or (S[0] != '0'):   # 排除以0 开头的非0数， 如 01 02 等
                    if int(S[:i]) < (2**31-1) and (len(current) < 2 or int(S[:i]) == int(current[-1]) + int(current[-2])):  # 数字限制；长度判断，如长度小于2，直接添加，如长度大于2，需判断和
                        current.append(S[:i])
                        if backtrack(S[i:], current):
                            return current
                        current.pop()

        result = backtrack(S, [])
        if result:
            return result
        else:
            return []