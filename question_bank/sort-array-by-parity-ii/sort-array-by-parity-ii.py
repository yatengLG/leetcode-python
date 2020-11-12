# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：244 ms, 在所有 Python3 提交中击败了79.21% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了21.67% 的用户

解题思路：
    单次遍历
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        num = 0
        i = 0
        while i < len(A):
            if A[i] % 2 == i % 2:   # 如果当前奇偶排序对应，则下一个元素
                i += 1
            else:
                while i+num < len(A) and A[i+num] % 2 != i % 2: # 找下一个满足奇偶排序的元素，并用num记录下标
                    num += 1
                A[i], A[i+num] = A[i+num], A[i] # 交换满足奇偶排序的项
                num -= 1    # 记录下标减1
                i += 1 # 处理下一个元素
        return A

"""
执行用时：232 ms, 在所有 Python3 提交中击败了91.19% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了13.33% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:    # 处理奇数下标
                while A[j] % 2: # 找偶数下标j对应的偶数
                    j += 2
                A[i], A[j] = A[j], A[i] # 交换i,j对应元素
        return A