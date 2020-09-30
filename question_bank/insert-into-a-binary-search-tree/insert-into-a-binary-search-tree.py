# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：164 ms, 在所有 Python3 提交中击败了73.44% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了81.96% 的用户

解题思路：
    在叶节点插入插入点
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        insert_node = TreeNode(val) # 待插入的节点
        def find(root):
            if root.val < val:  # 如果当前节点值小于插入值，遍历右子树
                if root.right:  # 如果右子树存在，遍历右子树
                    find(root.right)
                else:   # 如果不存在右子树，当前节点右节点为插入节点
                    root.right = insert_node
            else:   # 左子树同处理
                if root.left:
                    find(root.left)
                else:
                    root.left = insert_node
        if root:    # 如果树不为空， 开始遍历，插入插入节点点
            find(root)
            return root
        else:   # 如果当前树为空，则直接返回待插入节点
            return insert_node