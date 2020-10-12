# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了95.72% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了44.12% 的用户

解题思路：
    中序遍历
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.result = self.val = float('inf')   # 记录最终结果，以及当前节点值
        def find(root):
            if root:
                l = find(root.left)     # 先遍历左子树
                if l:
                    self.result = min(abs(self.val-l.val), self.result) # 判断节点差值绝对值，更新最小值
                    self.val = l.val

                self.result = min(abs(self.val - root.val), self.result)    # 根节点
                self.val = root.val

                r = find(root.right)    # 右子树
                if r:
                    self.result = min(abs(self.val - r.val), self.result)
                    self.val = r.val

        find(root)
        return int(self.result)