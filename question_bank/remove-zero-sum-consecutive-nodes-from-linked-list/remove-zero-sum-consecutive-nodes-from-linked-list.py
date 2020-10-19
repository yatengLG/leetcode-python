# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了95.06% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了5.35% 的用户

解题思路：
    i~j 和为0， 则必然 sum(0~i) == sum(0~j)
    且，每次删除后，需要重新从头计算，不然会出现中间删去部分又重复删去导致结果错误的情况
        [1, 3, 2, -3, -2, 5, 5, -5, 1]
      0  1  4  6   3   1  6  11  6  7
"""
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        start = ListNode(0, next=head)
        record = {0: start}
        add = 0
        while head:
            add += head.val
            if add in record:
                record[add].next = head.next    # 删除子链表
                return self.removeZeroSumSublists(start.next)   # 删去一个子链表后，重新计算
            else:
                record[add] = head
                head = head.next
        return start.next