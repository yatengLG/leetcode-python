# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了84.24% 的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了5.03%

解题思路：
    递归
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        def find(root, deep):   # 使用deep记录当前深度
            if root:
                if deep > len(result)-1:
                    result.append([])
                result[deep].append(root.val)   # 添加到最终结果的对应深度列表中
                find(root.left, deep+1)     # 处理左子树
                find(root.right, deep+1)    # 右子树
        find(root, 0)
        return result