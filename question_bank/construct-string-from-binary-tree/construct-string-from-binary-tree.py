# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了75.57% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了50.00% 的用户

解题思路：
    使用递归处理
    对于左节点有三种情况：存在，则返回节点值；若不存在，但右节点存在，则返回（）；若右节点也不存在，则返回“”
    对于右节点有两种情况：存在，则返回节点值；不存在，则返回“”
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if t.right:
            right = "({})".format(self.tree2str(t.right))
        else:
            right = ""

        if t.left:
            left = "({})".format(self.tree2str(t.left))
        else:
            if t.right:
                left = "()"
            else:
                left = ""
        return str(t.val)+left+ right