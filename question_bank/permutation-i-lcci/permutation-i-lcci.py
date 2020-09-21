# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：288 ms, 在所有 Python3 提交中击败了5.29% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了33.22% 的用户

解题思路：
    回溯
    通过一个列表记录已经使用过的字符下标
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        result = []
        def backtrack(current, used):
            if len(current) >= n:
                result.append(''.join(current[:]))

            for i in range(n):
                if i not in used:
                    backtrack(current+[S[i]], used+[i])
        backtrack([], [])
        return result


"""
执行用时：152 ms, 在所有 Python3 提交中击败了71.82% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了13.36% 的用户

解题思路：
    回溯
    更新当前字符串
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        result = []
        def backtrack(s, current):  # 当前剩余字符串
            if s == '':
                result.append(current)

            for i in range(len(s)):
                backtrack(s[:i]+s[i+1:], current+s[i])

        backtrack(S, '')
        return result

"""
"""