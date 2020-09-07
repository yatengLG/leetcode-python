# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了78.88% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了14.82% 的用户

解题思路：
    深度优先遍历
    并记录当前层数，便于结果存储

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res)<depth+1:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        return res[::-1]