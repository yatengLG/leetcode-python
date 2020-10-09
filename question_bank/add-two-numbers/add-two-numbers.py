# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了82.51% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.13%

解题思路：
    依次计算当前位和，并记录进位
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        l3 = l4 = ListNode(0)
        while l1 or l2 or add:
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            l3.next = ListNode(add % 10)
            add = add // 10
            l3 = l3.next
        return l4.next

