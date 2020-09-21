# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了98.56% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了18.48% 的用户

解题思路：
    先处理右子树，然后当前节点，然后处理左子树
    使用一个值，保存大于当前节点的节点值的总和
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.record = 0     # 用于记录大于当前节点的节点和
        def find(root):
            if root.right:  # 如果存在右子树
                find(root.right)    # 则继续处理右子树
            self.record += root.val # 处理完右子树后，将当前节点值添加到节点和中
            root.val = self.record  # 将当前节点值改为节点和
            if root.left:           # 处理左子树
                find(root.left)
        if root:
            find(root)
        return root