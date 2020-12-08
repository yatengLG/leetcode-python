# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了30.58% 的用户

解题思路：贪心算法
    tasks = ["A","A","A","B","B","B","C","C","C","D","E"], n = 2, leastInterval = 16

        A   B   C   D
        A   B   C   E
        A   B   C

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2, leastInterval = 16

        A   B   C
        A   D   E
        A   F   G
        A   _   _
        A   _   _
        A
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)  # 统计每个字符出现的次数
        h = max([v for _,v in count.items()])   # 选最大的作为矩形高
        w = len([v for _,v in count.items() if v == h]) # 将出现次数等于h的元素先放进矩阵，此时，矩阵宽w
        ew = max(math.ceil((len(tasks) - h*w)/h), n-w+1)    # 剩余字符放入矩阵，所需的额外宽ew

        if n - w + 1 > (len(tasks) - h * w) / h:    # 若剩余字符未放满ew*h
            num = h * w + max((len(tasks) - h * w), ew * (h - 1))
        else:                                       # 若剩余字符超出了ew*h, h * w + len(tasks) - h * w
            num = len(tasks)
        return num
