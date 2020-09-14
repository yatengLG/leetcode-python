# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了94.94% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了56.04% 的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if root == None:
            return result

        record = [root]
        while record:
            vals = [node.val for node in record]
            result.append(sum(vals) / len(vals))
            record_ = []

            for node in record:
                if node.left:
                    record_.append(node.left)

                if node.right:
                    record_.append(node.right)
            record = record_
        return result