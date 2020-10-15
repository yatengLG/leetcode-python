# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：76 ms, 在所有 Python3 提交中击败了85.75% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.31% 的用户

解题思路：
    将树中节点，以每层存入字典中。
    然后读取每层的节点，添加next指针
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        record = {} # 用于记录每层的节点

        def find(root, h):  # 递归遍历树，以高度从左到右将节点存入字典
            if root:
                if h in record:
                    record[h].append(root)
                else:
                    record[h] = [root]
                find(root.left, h+1)
                find(root.right, h+1)

        find(root, 0)
        for h, roots in record.items(): # 读取保存的字典，一层一层处理节点
            roots += [None]
            for i, r in enumerate(roots):
                if r:
                    r.next = roots[i+1]
        return root