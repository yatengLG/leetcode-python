# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了98.32% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了74.63% 的用户

解题思路：
    快慢指针

    |<----    l1   ---->|< --------
    1   2   3   4   5   6   7   8   l2
                        15      9   ↓
                        14      10  __
                        13  12  11

    从头部到入环 距离为 l1， 入环到快慢指针相遇点为l2， 环长 c

    则， 慢指针走过的距离为 s = 1 + l1 + l2
        快指针走过的距离为 f = l1 + l2 + nc  绕了环内走了n圈

    2s = f
    则，  2 + 2l1 + 2l2 = l1 + l2 + nc

    所求入环处 l1 = nc - l2 - 2
    nc - l2 可由 慢指针从相遇处 开始绕环走到入环处得来。
    即 在相遇时，从起点前两个距离开始，初始化一个指针， 同时慢指针从相遇处继续走。 新指针与慢指针会在入环处相遇
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s, f = ListNode(0, next= head), head    # 快慢指针

        while s != f:   # 相遇则有环，且当前位置为相遇处
            if f and f.next:
                s = s.next
                f = f.next.next
            else:   # 无环
                return
        # 有环时，初始化一个新指针，在开始前两个距离处
        new = ListNode(0, next=ListNode(0, next = head))    # 新指针

        while new != s: # 新指针与慢指针同时走，相遇处便是入环点
            new = new.next
            s = s.next

        return s