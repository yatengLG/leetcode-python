# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：160 ms, 在所有 Python3 提交中击败了94.60% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了7.93% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = ListNode(float('-inf'), next=head)
        r = result  # 指针r.next指向当前节点
        while r.next:   # 当前节点不为None时，
            if r.next.val > r.val:  # 如果当前节点后一个节点大于当前节点值，后移指针，处理下一个
                r = r.next
            else:   # 小于时，执行插入操作
                node = r.next   # 记录并删除当前节点node
                p = result
                r.next = r.next.next
                while p.next.val < node.val:    # 在排序好的链表中，寻找插入node的位置
                    p = p.next
                node.next = p.next  # 插入节点
                p.next = node
        return result.next