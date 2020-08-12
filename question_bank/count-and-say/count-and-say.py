# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了92.56% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了98.07% 的用户

解题思路：
    初始化 n为1时，return '1'
    当n>1时，开始循环，计算外观数列的第 n 项
    详细逻辑见代码注释
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'        # 初始的字符串为'1'， n为1时，外观数列也为'1'
        for _ in range(1, n):   # 当n>1时，依次循环计算外观数列
            s = ''              # s用于记录外观数列
            record_s = string[0]    # n-1外观数列的第一项， 待比较项
            record_n = 1            # 用于计数
            for i in range(1, len(string)): # 从第二项开始比较，字符是否相同
                if string[i] == record_s:   # 如果字符相同
                    record_n += 1           # 计数+1
                else:
                    s = s + str(record_n) + record_s    # 不相同时，写入s
                    record_s = string[i]                # 将待比较项 更新为当前不重复项
                    record_n = 1                        # 将计数 置为1
            s = s + str(record_n) + record_s            # 外观数列循环完，处理最后一项(或n项)
            string = s                                  # 将外观数列更新
        return string