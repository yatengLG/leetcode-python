# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了81.35% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    递归，获得每条支线节点组成的数字，然后相加
"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        record = []

        def find(root, current):
            current += str(root.val)
            if root.left == None and root.right == None:
                record.append(int(current))
                return
            else:
                if root.left:
                    find(root.left, current)
                if root.right:
                    find(root.right, current)

        if root:
            find(root, '')

        return sum(record)