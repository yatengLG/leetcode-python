# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了86.96% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了85.68% 的用户

解题思路：
    递归
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result =[]
        def find(root):
            if root:
                result.append(root.val)
                childrens = root.children
                for children in childrens:
                    find(children)
        find(root)
        return result