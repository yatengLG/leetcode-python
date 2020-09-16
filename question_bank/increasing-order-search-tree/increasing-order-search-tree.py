# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：24 ms, 在所有 Python3 提交中击败了99.87% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了65.60% 的用户

解题思路：
    递归
    先中序遍历，然后组成数
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def find(root):
            if root:

                find(root.left)
                result.append(root.val)
                find(root.right)
        find(root)
        # 建树
        start = now = TreeNode(0)
        for r in result:
            now.right = TreeNode(r)
            now = now.right

        return start.right