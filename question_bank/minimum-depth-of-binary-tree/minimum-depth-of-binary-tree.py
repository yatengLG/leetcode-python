# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了95.56% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了99.94% 的用户

解题思路：
    广度优先。
    具体实现见代码注释
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        roots = [root]  # 用于保存当前需要 查看的节点， 以根作为起始
        depth = 1       # 用于保存树的最小高度
        while roots:
            roots_c = []
            for r in roots:
                if r != None:   # 如果当前节点 为None，跳过，查看下一个节点
                    if r.left == None and r.right == None:  # 如果当前节点 左子树与右子树均为None, 则当前节点为叶节点，直接返回高度即可
                        return depth
                    else:       # 左右子树存在一个或多个，不是叶节点，则准备查看其左右子树
                        roots_c.append(r.left)
                        roots_c.append(r.right)
            roots = roots_c
            depth += 1  # 遍历完一次后，高度+1