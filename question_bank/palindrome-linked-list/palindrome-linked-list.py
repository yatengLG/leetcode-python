# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
执行用时：80 ms, 在所有 Python3 提交中击败了82.85% 的用户
内存消耗：23.8 MB, 在所有 Python3 提交中击败了67.04% 的用户

解题思路：
    快慢指针，使用慢指针找链表中心，将后半部分翻转
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head

        while fast and fast.next:   # 快慢指针，快指针是慢指针的2倍速,当快指针到达链表末尾时，慢指针刚好到一半
            fast = fast.next.next
            slow = slow.next

        reverse = None
        while slow: # 慢指针翻转链表后半部分
            i = slow
            slow = slow.next
            i.next = reverse
            reverse = i

        while head and reverse: # 进行比较
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True