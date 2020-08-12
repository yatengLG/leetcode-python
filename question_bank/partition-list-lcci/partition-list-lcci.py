# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了69.92% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    使用双指针，一个指针遍历，一个指针指向链头。
    若当前节点值小于阈值，则将当前节点挪到链头。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        if not head:
            return head
        while q.next:
            if q.next.val < x:
                r = q.next
                q.next = q.next.next
                r.next = p
                p = r
            else:
                q = q.next
        return p

