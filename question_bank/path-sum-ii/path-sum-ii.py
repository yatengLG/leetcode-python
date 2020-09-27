# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了62.60% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了25.28% 的用户

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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        def find(root, current, target):
            if root.left == None and root.right == None and target == root.val:
                result.append(current[:] + [root.val])
                return
            if root.left:
                find(root.left, current + [root.val], target - root.val)  # 回溯
            if root.right:
                find(root.right, current + [root.val], target - root.val)

        if root:
            find(root, [], sum)
        return result