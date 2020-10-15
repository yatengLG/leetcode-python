# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了95.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.26% 的用户

解题思路：
    回溯
    使用head记录已经访问过的节点，和新创建的对应节点
    实现详情见代码注释
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        def backtrack(head, visited):
            if head == None:    # None时，返回None
                return head

            if head in visited: # 如果head访问过了，返回对应的创建的新节点
                return visited[head]

            else:
                node = Node(head.val)   # 没有访问过，创新新节点
                visited[head] = node    # 将新创建的节点，与head绑定，记录到以访问
                node.next = backtrack(head.next, visited)   # 访问head节点的next
                node.random = backtrack(head.random, visited)   # 访问head节点的random
                return node

        node = backtrack(head, {})
        return node