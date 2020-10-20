# -*- coding: utf-8 -*-
# @Author  : LG


"""
执行用时：36 ms, 在所有 Python3 提交中击败了86.04% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.42% 的用户

解题思路：
    递归
    当遇到数字时，需要考虑连续数字组成的数字
    当遇到字母时，直接添加到最终结果中
    当遇到[]时，递归处理[]中的字符,
        遇到[时，下一个字符开始递归处理
        遇到]时，返回返回当前字符串, 即[]中字符串
    在递归过程中，因为[]中字符已经在递归中处理过了，在外面需要跳过，所以需要记录当前下标

    具体实现见代码注释
"""
class Solution:
    def decodeString(self, s: str) -> str:
        self.result = []
        self.s = s
        def find(i):    # 从s的第i个字符开始处理, 用于跳过[]中已递归处理过的字符
            r = ''      # 结果
            num = 0
            while i < len(self.s):  # 处理s中每个字符
                if self.s[i] in '0123456789':   # 是数字时，需要累计
                    num = num * 10 + int(self.s[i])
                elif self.s[i] == '[':  # 开启递归，处理[]中字符
                    rs, ri = find(i+1)  # 返回[]中字符，以及]的下标
                    r = r + num * rs
                    i = ri  # 跳过[]中已处理过的字符
                    num = 0 # 重置num
                elif self.s[i] == ']':  # ]时，需要返回当前字符串，和当前]的下标
                    return r, i
                else:   # 字母时，直接添加到当前字符串
                    r += self.s[i]
                i += 1
            return r    # 处理完所有字符后, 即为最终结果
        return find(0)