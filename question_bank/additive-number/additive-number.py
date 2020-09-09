# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了65.97% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了54.62% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def backtrack(num, current):
            # print(num, current)
            if num == '' and len(current) > 2:  # 如果当前划分大于2，且字符串均处理完成，则返回True
                return True
            if num == '':   # 如果字符串均处理完，则跳出
                return
            for i in range(1, n):
                if (num[0] == '0' and i < 2) or num[0]!='0':    # 针对以0开头的数字处理，如02 03
                    if len(current)<2 or (len(current) >= 2 and int(num[:i])==int(current[-1])+int(current[-2])):   # 如当前数字个数小于2，则直接添加。如大于2，则需判别是否和等于前两个数想加
                        current.append(num[:i])
                        new_num = num[i:]
                        if backtrack(new_num, current): # 在剩余字符串中寻找下一个数字
                            return True
                        current.pop()   # 回溯

        return backtrack(num, [])
