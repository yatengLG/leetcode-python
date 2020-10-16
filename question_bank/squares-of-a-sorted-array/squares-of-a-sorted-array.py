# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：296 ms, 在所有 Python3 提交中击败了45.62% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.22% 的用户

解题思路：
    先处理小于0的值，平方后直接添加到最终结果中
    然后处理>=0的值，并用一个q指针记录在result中的插入位置
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [a**2 for a in A if a<0][::-1]
        pos = [a**2 for a in A if a>=0]
        # print(pos, result)
        q = 0
        for p in pos:
            if result == [] or p > result[-1]:
                result += [p]
            else:
                while p > result[q]:
                    q = q + 1
                result.insert(q, p)
        return result

"""
执行用时：284 ms, 在所有 Python3 提交中击败了56.45% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.22% 的用户
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [a**2 for a in A]
        result.sort()
        return result