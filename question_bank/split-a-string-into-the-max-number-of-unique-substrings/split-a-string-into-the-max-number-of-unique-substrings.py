# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    回溯+剪枝
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0

        def backtrack(s, current):

            if s == '':     # 如果字符串处理完成，则对比当前结果长度，更新结果
                if len(current) > self.result:
                    self.result = len(current)
                return

            if len(current) + len(s) <= self.result:    # 剪枝，如果当前剩余字符串长度+ 当前列表长度小于 最终结果，则跳出
                return

            for i in range(1, len(s)+1):    # 处理当前剩余的字符串
                if s[:i] not in current:
                    backtrack(s[i:], current+[s[:i]])

        backtrack(s, [])
        return self.result


"""
超出时间限制
思路：
    回溯，列举所有结果，然后对比
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = []

        def backtrack(s, current):
            print(s, current)
            if s == '':
                result.append(current[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] not in current:
                    backtrack(s[i:], current+[s[:i]])

        backtrack(s, [])
        result = [len(r) for r in result]
        return max(result)