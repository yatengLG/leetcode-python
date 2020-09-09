# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：3088 ms, 在所有 Python3 提交中击败了5.31% 的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了5.19% 的用户

解题思路：
    回溯
    出版，使用current存放当前列表，通过len(current)获取即将插入的下标
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current):
            # print(current)
            if len(current) == N:
                result.append(current[:])
                return

            for i in range(N):
                if nums[i] not in current and (nums[i] % (len(current)+1) == 0  or (len(current)+1) % nums[i] == 0):
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()

        backtrack([])
        return len(result)

"""
执行用时：2536 ms, 在所有 Python3 提交中击败了9.78% 的用户
内存消耗：21.8 MB, 在所有 Python3 提交中击败了5.19% 的用户

优化思路：
    直接从nums中取数字，可以提升一部分
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current):
            if len(current) == N:
                result.append(current[:])
                return

            for num in nums:
                if num not in current and (num % (len(current)+1) == 0  or (len(current)+1) % num == 0):
                    current.append(num)
                    backtrack(current)
                    current.pop()

        backtrack([])
        return len(result)

"""
执行用时：2240 ms, 在所有 Python3 提交中击败了15.64% 的用户
内存消耗：21.6 MB, 在所有 Python3 提交中击败了5.19% 的用户

优化思路：
    使用一个单独的index变量，记录存储在列表中的位置。
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current, index):
            if len(current) == N:
                result.append(current[:])
                return

            for num in nums:
                if num not in current and (num % index == 0  or index % num == 0):
                    current.append(num)
                    backtrack(current, index+1)
                    current.pop()

        backtrack([], 1)
        return len(result)
