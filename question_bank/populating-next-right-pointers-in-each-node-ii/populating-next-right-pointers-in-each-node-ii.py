# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了81.56% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了54.12% 的用户

解题思路：
    先把每层的节点以自左向右的顺序保存，
    然后修改next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        record = {}
        def find(root, h):  # 遍历，并保存每层的节点
            if root:
                if h in record:
                    record[h].append(root)
                else:
                    record[h] = [root]
                find(root.left, h+1)    # 自左向右的顺序遍历
                find(root.right, h+1)

        find(root, 1)
        for h, ns in record.items():    # 处理每层的节点
            for i in range(len(ns)-1):
                ns[i].next = ns[i+1]
            ns[-1] = None
        return root