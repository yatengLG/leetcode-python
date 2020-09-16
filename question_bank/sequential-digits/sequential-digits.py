# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了67.71% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了7.21% 的用户

解题思路：
    回溯
    一次以1~9开头，查看符合要求的数字
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        def backtract(now, current):    # 以now开头， current记录当前数字
            if low <= current <= high:  # 符合题意，添加到最终结果
                result.append(current)
            if now >= 9 or current > high:
                return
            backtract(now+1, current*10+now+1)

        for i in range(1, 10):  # 以1~9依次作为开头
            backtract(i, i)
        result.sort()
        return result