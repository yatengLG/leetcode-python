# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：84 ms, 在所有 Python3 提交中击败了61.57% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.00% 的用户

解题思路:
    具体实现见代码注释
"""
class Solution:
    def sortString(self, s: str) -> str:
        s_list = list(s)    # 字符串转列表
        result = []         # 保存最终结果
        reverse = False     # 翻转顺序
        while s_list:
            rs = list(set(s_list))  # 去重
            rs.sort(reverse=reverse)    # 排序

            result.extend(rs)   # 添加到最终结果中
            for r in rs:
                s_list.remove(r)    # 从列表中移除已经添加的数据
            reverse = not reverse   # 翻转

        return ''.join(result)