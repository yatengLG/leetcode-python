# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.26% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.00% 的用户

解题思路：
    递归
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def find(root):
            if root:
                result.append(root.val)
                find(root.left)
                find(root.right)

        find(root)
        return result