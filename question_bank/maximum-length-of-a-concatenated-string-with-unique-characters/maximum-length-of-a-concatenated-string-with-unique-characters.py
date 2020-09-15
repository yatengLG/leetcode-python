# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：156 ms, 在所有 Python3 提交中击败了34.91% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了7.28% 的用户

解题思路：
    回溯
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = []    # 用于存放所有结果
        n = len(arr)

        def backtrack(begin, current:str):  # 起始位置，当前合并字符串
            results.append(current) # 把当前结果存入最终结果中
            if begin == n:  # 如果遍历结束，则结束
                return
            for i in range(begin, n):   # 从起始位置一直向后遍历
                if len(set(current+arr[i])) != len(current+arr[i]): # 如果当前字符串存在重复元素，则跳出，继续下一个
                    continue
                backtrack(i, current+arr[i])    # 处理下一个字符串
                # 因为是字符串，且，传入的是current+arr[i], 这里不需要进行额外处理
        backtrack(0, '')
        result = 0
        for r in results:
            if len(r) > result:
                result = len(r)
        return result


"""
执行用时：156 ms, 在所有 Python3 提交中击败了34.91% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了96.12% 的用户

代码经过精简后
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.result = 0
        n = len(arr)

        def backtrack(begin, current:str):

            if len(current) > self.result:
                self.result = len(current)

            for i in range(begin, n):
                if len(set(current+arr[i])) != len(current+arr[i]):
                    continue
                backtrack(i, current+arr[i])

        backtrack(0, '')

        return self.result