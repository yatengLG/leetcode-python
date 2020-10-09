# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.98% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了19.40% 的用户

解题思路：
    双指针。分别指向列表首尾，然后交换指针指向元素
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l, r = 0, n-1   # 左右指针分别指向首尾
        while r > l:
            s[l], s[r] = s[r], s[l] # 交换元素
            l += 1  # 移动指针
            r -= 1