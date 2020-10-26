# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了99.89% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.09% 的用户

解题思路：
    统计num出现的次数
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        record1, record2 = [0] * 101, [0] * 101

        for num in nums:
            record1[num] += 1   # 统计每个数出现的次数

        for i in range(1, 101):
            record2[i] = record1[i-1] + record2[i-1]    # 计算比当前数小的数的个数

        result = []
        for num in nums:
            result += [record2[num]]
        return result


"""
执行用时：112 ms, 在所有 Python3 提交中击败了50.42% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了8.85% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        record = {} # 统计比当前数小的数个数
        record_n = defaultdict(int) # 统计当前数的出现次数
        for num in nums:
            if num in record:
                record_n[num] += 1
                continue
            record[num] = 0

            for r in record:
                if r > num:
                    record[r] += 1
                elif r < num:
                    record[num] += 1

        result = []
        for num in nums:
            n = record[num] # 最终结果，小于当前数的个数+每个小于当前数的数的出现次数
            for rn in record_n:
                if rn < num:
                    n += record_n[rn]
            result += [n]
        return result