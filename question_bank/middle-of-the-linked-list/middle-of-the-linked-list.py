# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了94.94% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.29% 的用户

解题思路：
    快慢指针
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s, f = head, head   # 快慢指针
        while f and f.next:
            s = s.next
            f = f.next.next
        return s