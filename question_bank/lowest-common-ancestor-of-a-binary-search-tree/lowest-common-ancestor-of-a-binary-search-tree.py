# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
执行用时：80 ms, 在所有 Python3 提交中击败了99.61% 的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了86.69% 的用户

解题思路：
    因为是二叉搜索树，左节点值必定小于右节点。
    如果当前节点值处于俩个指定节点之间，则最近公共祖先必定为当前节点。
    若不是，通过比较节点值，对树进行更新
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l_val, r_val = p.val, q.val
        if l_val > r_val:       # 确保指定节点值大小顺序
            l_val, r_val = r_val, l_val

        while True:
            if l_val <= root.val <= r_val:  # 当前节点处于指定两节点之间
                return root

            if root.val > r_val:    # 当前节点小于指定节点最小值，更新当前节点为节点左子树
                root = root.left
            if root.val < l_val:    #
                root = root.right