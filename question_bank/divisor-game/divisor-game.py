# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了56.79% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了25.00% 的用户
解题思路：
    以极限情况，按每次取1来解。
    以偶数开始，若爱丽丝先选必赢
    以奇数来选，爱丽丝必输
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N%2 ==0