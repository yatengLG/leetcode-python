# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了96.73% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了23.93% 的用户

解题思路：
    快慢指针
    若存在环，快指针会先入环，慢指针后如环。在环中，快慢指针相遇，返回True
    若不存在环，快指针先到达链表末尾
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l, f = ListNode(0, next=head), head # 慢指针，快指针
        while l != f:   # 快慢指针不同，循环
            if f and f.next:
                l = l.next  # 慢指针走一步
                f = f.next.next # 快指针走两步
            else:
                return False    # 若达到链表末尾，则无环
        return True