# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了95.78% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了17.49% 的用户

解题思路：
    先寻找两节点在树中的位置
    保存，节点的深度和父节点
    具体实现见代码注释
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        record = {} # 用于保存  x,y在树中的深度和父节点
        def find(root, f, h):
            if root:
                if root.val == x or root.val == y:  # 找到x,y
                    record[root.val] = [f, h]       # 记录x,y的父节点和深度
                    return
                find(root.left, root, h+1)
                find(root.right, root, h+1)

        find(root, None, 0)

        if len(record) == 2:    # 如果x,y都找到
            if record[x][1] == record[y][1] and record[x][0] != record[y][0]:   # xy处于同深度，且父节点不同时，返回true
                return True
            else:
                return False
        else:
            return False