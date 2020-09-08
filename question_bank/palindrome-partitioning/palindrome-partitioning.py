# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了78.43% 的用户
内存消耗：14 MB, 在所有 Python3 提交中击败了55.73% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(s, current):  # 当前字符串， 当前结果
            if s == '':             # 如果字符串都处理完，添加到最终结果
                result.append(current[:])
                return

            for i in range(1, len(s)+1):
                if huiwen(s[:i]):               # 如果当前s[:i]回文
                    current.append(s[:i])       # 添加到当前结果中
                    backtrack(s[i:], current)   # 在剩余字符串s[i:]中寻找回文
                    current.pop()               # 回溯

        def huiwen(s):
            if s == s[::-1]:
                return True
            else:
                return False

        backtrack(s, [])
        return result