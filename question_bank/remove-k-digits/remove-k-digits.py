# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了69.82% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了6.73% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        self.k = k
        def insert(c):  # 插入c字符
            # print(c, self.k, result)
            if result == [] or self.k < 1 or c >= result[-1]:   # 如果result为空，k<1，或者当前c大于栈顶元素， c入栈
                result.append(c)
            else:   # 否则，出栈一个字符，重新尝试插入c
                result.pop()
                self.k -= 1
                insert(c)

        for c in num:   # 一次插入num中数字
            if self.k > 0:
                insert(c)
            else:
                result.append(c)

        for i in range(self.k): # 当k>1时，如果栈不空，则继续出栈
            if result:
                result.pop()
        if result == []:
            result = ['0']
        return str(int(''.join(result)))
