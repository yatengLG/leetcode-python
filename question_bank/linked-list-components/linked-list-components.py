# -*- coding: utf-8 -*-
# @Author  : LG


"""
执行用时：100 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    遍历链表，查看是否存在与G中，如存在，就算一个组件，直到下次出现断开的情况
    添加了G = set(G)
"""
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        num = 0
        start = False   # 用于记录是否连续
        while head:
            if head.val in G:
                G.remove(head.val)
                if not start:   # 与前面不连续，则为一个新租件
                    start = True
                    num += 1
            else:   # 当前值不在G中，断开
                start = False
            head = head.next
        return num