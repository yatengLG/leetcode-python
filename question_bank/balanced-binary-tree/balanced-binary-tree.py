# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了92.70% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了44.80% 的用户

解题思路：
    递归
    在实现时，参考了官方提供的思路。
    从叶节点开始，一直向上进行判断。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:    # 叶节点，高度为0
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height)>1:    # -1 来表示 子树高度大于1 的情况
                return -1
            else:
                return max(left_height, right_height) + 1   # 如果平衡，则该节点的root高度为 叶节点最大高度+1

        return height(root)>=0