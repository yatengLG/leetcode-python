# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：108 ms, 在所有 Python3 提交中击败了96.06% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了25.37% 的用户

解题思路：
    先在树中找到与链表第一个节点相同值的 树节点
    然后以这些树中节点为根的子树中寻找是否存在链表
"""
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def Sub(root, head):    # 递归在子树中判断是否当前子树存在链表
            # print(root, head)
            if head==None:  # 如果链表匹配完，则返回True，存在
                return True

            elif root and head:
                if root.val == head.val:
                    if Sub(root.left, head.next):
                        return True
                    if Sub(root.right, head.next):
                        return True

        nodes = []
        def find(root, head):   # 递归寻找树中所有与链表首节点值相同的树节点
            if root:
                if root.val == head.val:    # 如果当前节点值等于链表首节点值，记录
                    nodes.append(root)
                find(root.left, head)
                find(root.right, head)
        find(root, head)

        for node in nodes:
            if Sub(node, head): # 判断所有子树是否存在
                return True
        return False