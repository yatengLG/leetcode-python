# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了93.86% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了66.25% 的用户

解题思路：
    单指针去重
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next: # 如果未到末尾
            if p.val == p.next.val: # 如果相等，则删掉重复的元素
                p.next = p.next.next
            else:
                p = p.next  # 不重复则移动指针
        return head