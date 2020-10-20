# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了98.66% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.45% 的用户

解题思路：
    栈
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        result = [] # 最终结果列表
        path = path.split('/')  # 以/拆分路径，多个//拆分后为''空字符
        for p in path:
            if p == '' or p == '.': # 如果是''空字符，或'.'当前路径，则忽略
                pass
            elif p == '..':         # '..'上一级目录，出栈
                if result:
                    result.pop()
            else:
                result.append(p)    # 其他情况为路径，入栈
        return '/' + '/'.join(result)   # 格式化，路径之间添加/， 首位置添加/