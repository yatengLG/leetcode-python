# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：76 ms, 在所有 Python3 提交中击败了61.41% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    使用双指针分别遍历两个链表，使用一个数记录进位。
    若双指针与进位均空时，结束。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        head = o = ListNode(0)
        add = 0

        while (p or q or add):

            if p:
                add = p.val + add
                p = p.next
            if q:
                add = q.val + add
                q = q.next
            o.next = ListNode((add % 10))
            o = o.next
            add = add // 10

        return head.next