# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了64.10% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了79.35% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def find(root1, root2): # 两棵树的对应节点
            if root1 and root2: # 如果节点都存在
                node = TreeNode(root1.val + root2.val)  # 合并后的当前节点为两树节点和
                node.left = find(root1.left, root2.left)    # 处理两树的对应左子树， 返回的节点为当前合并子树的左子树
                node.right = find(root1.right, root2.right) # 处理两树的对应右子树

            elif root1 or root2:    # 只存在一个节点
                node = TreeNode(root1.val if root1 else root2.val)  # 当前节点等于存在节点值
                node.left = find(root1.left if root1 else None, root2.left if root2 else None)  # 遍历存在节点的左子树
                node.right = find(root1.right if root1 else None, root2.right if root2 else None)   # 遍历存在节点的右子树
            else:
                return None # 均不存在返回None
            return node
        t = find(t1, t2)
        return t


"""
执行用时：100 ms, 在所有 Python3 提交中击败了91.61% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了46.33% 的用户

解题思路：
    同上，但不新建树
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def find(root1, root2): # 两棵树的对应节点
            if root1 and root2: # 如果节点都存在
                root1.val = root1.val + root2.val  # 合并后的当前节点为两树节点和
                root1.left = find(root1.left, root2.left)    # 处理两树的对应左子树， 返回的节点为当前合并子树的左子树
                root1.right = find(root1.right, root2.right) # 处理两树的对应右子树

            elif root1 or root2:    # 只存在一个节点, 直接返回存在的节点即可
                return root1 if root1 else root2
            else:
                return None # 均不存在返回None
            return root1
        t = find(t1, t2)
        return t