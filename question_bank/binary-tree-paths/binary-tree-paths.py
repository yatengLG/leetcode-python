# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.78% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了5.78% 的用户

解题思路：
    回溯
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []

        def find(root, current: list):
            if root == None:    # 如果当前节点是none，则终止
                return

            current.append(root.val)    # 不是none，将当前节点添加到当前列表中

            if root.left == None and root.right == None:    # 当前节点是叶节点时，将当前列表添加到最终结果中
                result.append('->'.join([str(n) for n in current]))

            find(root.left, current)    # 遍历左子树
            find(root.right, current)   # 遍历右子树
            current.pop()               # 回溯

        find(root, [])
        return result