# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.45% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.09% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        record = {} # 记录字符串中每个字符出现的次数
        for c in s:
            if c in record:
                record[c] += 1
            else:
                record[c] = 1
        result = []     # 保存最终结果

        def insert(c):  # 执行插入c字符
            if c not in result: # 当前结果中不存在c字符
                if result and result[-1] >= c and record[result[-1]] > 1:   # 如过结果中前一个字符存在多个，且比当前字符c大， 则将前一个字符出栈
                    record[result.pop()] -= 1       # 前一个字符从统计数-1
                    insert(c)   # 接着尝试插入c字符
                elif c not in result:
                    result.append(c)
                    # record[c] -= 1
            else:   # 如果当前结果中存在字符c，跳过，字典中c的统计-1
                record[c] -= 1
        for c in s: # 挨个插入s字符串中的字符
            insert(c)
        return ''.join(result)
