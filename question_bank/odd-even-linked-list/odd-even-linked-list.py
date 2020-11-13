# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了99.25% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.20% 的用户

解题思路：
    双指针
    具体实现见代码注释
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not (head and head.next and head.next.next):
            return head

        p, q = head, head.next  # 双指针，p指向插入处，q指向待插入节点前一个

        while q and q.next:
            node = q.next       # 取出node
            q.next = node.next  # 删掉node，连接删后的链表

            p_next = p.next     # 记录p的下一个节点
            p.next = node       # 插入node
            node.next = p_next  # 连接链表

            p = p.next  # 移动指针
            q = q.next
        return head