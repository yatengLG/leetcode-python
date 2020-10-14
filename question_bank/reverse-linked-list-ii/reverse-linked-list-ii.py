# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了91.22% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了9.56% 的用户

解题思路：
    先找到需要反转的链表起始处
    使用p,q双指针反转链表，使用r指针记录反转的后一个节点
    最后连接链表
"""
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        result = ListNode(0, next=head)
        pre = result
        for i in range(m-1):    # 先找到需要翻转的节点的前一个
            pre = pre.next

        p = pre.next    # p,q 指向当前需要交换的两个节点
        q = p.next
        for _ in range(m,n):
            r = q.next  # 记录q的下一个节点
            q.next = p  # 反转节点
            p = q
            q = r
        pre.next.next = q   # 连接链表
        pre.next = p
        return result.next