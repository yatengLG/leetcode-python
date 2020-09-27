# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：192 ms, 在所有 Python3 提交中击败了56.79% 的用户
内存消耗：86.4 MB, 在所有 Python3 提交中击败了5.01% 的用户


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def find(inorder, postorder):
            if inorder == []:
                return
            node = postorder[-1]    # 后续遍历的最后一个为当前树的根
            node_index = inorder.index(node)    # 中序遍历中，根左侧为左子树节点，右侧为右子树节点

            node = TreeNode(node)   # 当前节点
            node.left = find(inorder[:node_index], postorder[:node_index])  # 划分左子树中序及后序
            node.right = find(inorder[node_index+1:], postorder[node_index:-1]) # 划分右子树中序及后序
            return node

        t = find(inorder, postorder)
        return t