# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了97.99% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了5.05% 的用户

解题思路：
    指针+递归
    具体实现见代码注释
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        result = Node(0)    # 用于保存结果
        self.node = result  # 指针指向当前处理节点
        def find(head): # 递归
            if head:
                head_next = head.next   # 保存当前节点next和child
                head_child = head.child

                self.node.next = head   # 将当前节点插入到指针后
                self.node.child = None  # 删除child
                head.prev = self.node
                self.node = self.node.next  # 移动指针

                find(head_child)    # 递归处理child
                find(head_next)     # 递归处理next
        find(head)
        if head:
            result.next.prev = None # 将结果的prev指向None
        return result.next