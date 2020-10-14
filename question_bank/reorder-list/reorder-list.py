# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了99.84% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了32.31% 的用户

解题思路：
    先前后两部分断开链表，将后半部分反转后，一一插入前半部分
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not (head and head.next and head.next.next): # 如果链表长度小于3，直接返回当前链表
            return

        s, f = head, head   # 快慢指针，断开链表
        while f and f.next:
            s = s.next
            f = f.next.next

        p = s.next  # 需要翻转的后半段链表的头
        q = p.next  # q指向p的下一个节点
        p.next = None   # 断开p节点，不然反转后的后半段会存在环
        s.next = None   # 断开链表

        while q:    # 反转链表
            r = q.next
            q.next = p
            p = q
            q = r

        h = head
        while p:    # 将翻转后的后半段链表，一一插入前半段链表中
            h_next = h.next
            p_next = p.next
            h.next = p
            p.next = h_next
            h = h_next
            p = p_next