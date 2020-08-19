# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：648 ms, 在所有 Python3 提交中击败了9.86% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了79.30% 的用户

解题思路：
    暴力法, 双指针暴力拆解
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num = 0
        for i in range(n):
            for j in range(i, n):
                string = s[i:j+1]
                if string == string[::-1]:
                    num += 1
        return num

"""
执行用时：164 ms, 在所有 Python3 提交中击败了65.42% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了62.96% 的用户

解题思路：
    中心扩展, 需分析两种情况    xax, xaax 以单个字符为中心，以两个字符为中心
    详见代码注释
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num = 0
        i = 0
        while i < n:        # i指针，依次遍历字符串
            num += 1        # 每个单独的字符都回文
            l, r = i, i     # 以当前字符为中心，向两侧扩展
            while l-1 >= 0 and r+1 < n:
                if s[l-1] == s[r+1]:    # 判断字符两侧是否相同，若相同，则该字符串回文
                    num += 1
                    l = l-1             # 相同继续扩展
                    r = r+1
                else:
                    break               # 不相同，则跳出循环，遍历下一个字符

            if i+1<n and s[i+1] == s[i]:    # 判断当前点与下一个点是否相同，若相同，则相邻两字符回文
                num += 1                    # 若相同，则相邻两字符回文
                l, r = i, i+1               # 以两字符开始向外扩展

                while l - 1 >= 0 and r + 1 < n:
                    if s[l - 1] == s[r + 1]:    # 两侧字符相同，则组成的字符串回文
                        num += 1
                        l = l - 1               # 继续扩展
                        r = r + 1
                    else:
                        break
            i += 1
        return num

