# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.79% 的用户
内存消耗：13.2 MB, 在所有 Python3 提交中击败了94.96% 的用户

解题思路：
    递归
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def find(root):
            if root:
                find(root.left) # 先处理左节点
                find(root.right)    # 再处理右节点
                result.append(root.val) # 最后处理当前节点
        find(root)
        return result