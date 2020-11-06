# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了26.50% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了25.81% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        record = dict() # {int:list} 出现int次1 的各数组成的列表
        for i in range(len(arr)):
            a = arr[i]
            num = 0
            while a > 0:
                num += (a == a | 1) # 看最后位是否是1
                a = a >> 1  # 右移
            if num not in record:   # 存入字段
                record[num] = [arr[i]]
            else:
                record[num].append(arr[i])
        result = []
        keys_sort = list(record.keys()) # 对字典key进行排序
        keys_sort.sort()
        for key in keys_sort:
            record[key].sort()
            result.extend(record[key])
        return result

"""
执行用时：68 ms, 在所有 Python3 提交中击败了20.30% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了22.39% 的用户

解题思路：
    将数转换为二进制，然后统计出现的1.然后排序
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x:(bin(x).count('1'), x))
        return arr