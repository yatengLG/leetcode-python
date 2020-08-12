# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
执行用时：84 ms, 在所有 Python3 提交中击败了85.44% 的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了22.15% 的用户

解题思路：
    存在以下三种情况：
        1. 当前根节点 等于指定节点，则另一个节点肯定存在于当前节点的子树中，当前节点为最近公共祖先
        2. 指定节点分别存在与当前节点的左右子树中，当前节点为最近公共祖先
        3. 若都存在于同侧子树中，下移根节点，在本侧子树中寻找
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if right and left:
            return root
        if right:
            return right
        if left:
            return left
