# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
执行用时：40 ms, 在所有 Python3 提交中击败了82.14% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了87.69% 的用户

解题思路：
    双指针，单次循环
    [1,2,3,4,5]n = 2

       i      j
    record -> 1 -> 2 -> 3 -> 4 -> 5 -> None         # 双指针

       i                j
    record -> 1 -> 2 -> 3 -> 4 -> 5 -> None         # 先移动j指针，n步

                        i              j
    record -> 1 -> 2 -> 3 -> 4 -> 5 -> None         # 然后一起移动i, j指针，直到j为None

                        i              j
    record -> 1 -> 2 -> 3 -> 4 -> 5 -> None         # 此时i指针指向的下一个元素即为需要删除的元素
                        |---------|
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        record = ListNode(0)
        record.next = head
        i, j = record, head

        for _ in range(n):
            j = j.next

        while j:
            i = i.next
            j = j.next
        i.next = i.next.next

        return record.next