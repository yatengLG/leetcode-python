# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了94.98% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了24.06% 的用户

解题思路：
    见代码注释
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.result = 0
        def find(root):
            left = root.left    # 当前节点左子树
            right = root.right  # 当前节点右子树
            if left:            # 如果左子树不为None
                if not (left.left or left.right):   # 如果该左子树是叶节点，添加到最终结果中
                    self.result += left.val
                else:
                    find(left)  # 如不是叶节点，处理该节点
            if right:   # 如果右子树2不为None, 处理该节点
                find(right)
        if root:
            find(root)
        return self.result