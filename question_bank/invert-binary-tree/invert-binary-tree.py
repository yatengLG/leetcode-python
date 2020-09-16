# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.80% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了6.61% 的用户

解题思路：
    递归，翻转二叉树左右子树即可
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root:
                root.left, root.right = root.right, root.left

                invert(root.left)
                invert(root.right)
        invert(root)
        return root