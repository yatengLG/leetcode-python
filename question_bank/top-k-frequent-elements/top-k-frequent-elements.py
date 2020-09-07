# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了98.35% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了83.91% 的用户

解题思路：
    先遍历整个列表，统计每个数字出现的次数
    然后翻转字典，统计出现次数，并排序，从翻转字典中查找对应的数字
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            if num not in record:
                record[num] = 1
            else:
                record[num] += 1

        record_ = {}
        for key, value in record.items():
            if value not in record_:
                record_[value] = [key]
            else:
                record_[value].append(key)

        value = list(record.values())
        value.sort(reverse=True)

        result = []
        if k == 1:
            result.extend(record_[value[0]])
            return result

        for k in set(value[:k]):
            result.extend(record_[k])
        return result