# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了75.22% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了20.87% 的用户

解题思路：
    贪心算法，排序后，前面的区间，起始均小于等于后面区间起始。
    若想删除最少的区间，只需保证每次保留末尾靠前的区间即可。

    对于两个区间[a1, a2], [b1, b2]共分三种情况：
        1.  存在交叉, 删除后一个区间
            a1,     a2
                b1,    b2

        2.  存在并集， 删除前一个区间
            a1,         a2
                b1, b2
        3.  无交叉， 不需要删除
            a1, a2
                b1, b2

            a1, a2
                    b1, b2

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        i = 0
        j = 1
        while i+j < len(intervals):
            # print(i, j, intervals[i], intervals[j+i], result)
            if intervals[i+j][0] < intervals[i][1] <= intervals[i+j][1]: # 存在交叉， 则跳过后一个区间，继续匹配
                result += 1
                j += 1
            elif intervals[i+j][1] <= intervals[i][1]:  # 后一个区间包含在当前区间内， 则以后一个区间继续匹配
                result += 1
                i = i + j
                j = 1
            else:   # 如果不存在交叉，则处理下一个区间
                i = i+j
                j = 1
        return result