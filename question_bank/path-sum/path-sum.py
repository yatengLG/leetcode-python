# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了94.04% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了26.11% 的用户

解题思路：
    递归
    具体实现见代码注释
"""
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def find(root, current):
            if root:
                current += root.val
                if root.left:
                    if find(root.left, current):    # 处理左子树
                        return True
                if root.right:
                    if find(root.right, current):   # 处理右子树
                        return True
                if not (root.left or root.right):   # 如果是叶节点，判断当前和
                    if current == sum:
                        return True
        if find(root, 0):
            return True
        else:
            return False