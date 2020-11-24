# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.13% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了66.55% 的用户

解题思路：
    自定义排序
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_dic = {a:i for i, a in enumerate(arr2)}    # 将arr2 按 元素:顺序 组成字典
        arr1.sort(key=lambda x:sort_dic[x] if x in sort_dic else len(arr2)+x) # 如果在字典中，则按照字典顺序排序，如不在字典中，则按照x本来的值排序
        return arr1
