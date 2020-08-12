# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了64.00% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了81.91% 的用户

解题思路：
    建一个新链用于存放链接后的链表，依次比较两个列表。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        record = ListNode(0)
        new = record
        while l1 and l2:    # 俩个列表均不为空时,依次比较两个列表
            if l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next

        if l1:              # 如果l1剩下的列表非空，则直接加入新列表中
            new.next = l1

        if l2:
            new.next = l2


        return record.next
