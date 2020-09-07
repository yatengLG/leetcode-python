# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：652 ms, 在所有 Python3 提交中击败了17.13% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了33.38% 的用户

解题思路：
    回溯
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        result = []
        def backtrack(i, current):
            if len(current) == k:
                result.append(current[:])
                return
            for j in range(i, n):
                if nums[j] not in current:
                    current.append(nums[j])
                    backtrack(j + 1, current)   # 下一个
                    current.pop()               # 回溯
        backtrack(0, [])
        return result

"""
执行用时：60 ms, 在所有 Python3 提交中击败了85.87% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了83.56% 的用户

解题思路：
    回溯
    在上例代码中添加剪汁操作
    具体实现见代码注释
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        result = []
        def backtrack(i, current):
            # print(current)
            if len(current) == k:
                result.append(current[:])
                return

            for j in range(i, n):
                if n - j < k - len(current):    # n-j 为当前剩余的数的个数，k-len(current)为当前还缺少的数量。如果不够时，直接跳过。
                    break
                current.append(nums[j])
                backtrack(j + 1, current)
                current.pop()
        backtrack(0, [])
        return result