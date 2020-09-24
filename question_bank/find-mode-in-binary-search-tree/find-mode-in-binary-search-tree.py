# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了99.56% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了43.30% 的用户

解题思路：
    具体实现见代码注释
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        record = {}         # 用于保存每个节点出现的次数
        def find(root):     # 递归
            if root:
                if root.val not in record:
                    record[root.val] = 1
                else:
                    record[root.val] += 1
                find(root.left)
                find(root.right)

        find(root)
        result = {} # 各出现次数的节点
        for k, v in record.items():
            if v not in result:
                result[v] = [k]
            else:
                result[v].append(k)
        return result[sorted(result.keys())[-1]]    # 返回出现次数最多的节点