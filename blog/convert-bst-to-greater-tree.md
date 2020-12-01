Leetcode 538. 把二叉搜索树转换为累加树
<p>给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。</p>


<p>&nbsp;</p>



<p><strong>例如：</strong></p>



<pre><strong>输入:</strong> 原始二叉搜索树:

              5

            /   \

           2     13



<strong>输出:</strong> 转换为累加树:

             18

            /   \

          20     13

</pre>



<p>&nbsp;</p>



<p><strong>注意：</strong>本题和 1038:&nbsp;<a href="https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/">https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/</a> 相同</p>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了98.56% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了18.48% 的用户

解题思路：
    先处理右子树，然后当前节点，然后处理左子树
    使用一个值，保存大于当前节点的节点值的总和
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.record = 0     # 用于记录大于当前节点的节点和
        def find(root):
            if root.right:  # 如果存在右子树
                find(root.right)    # 则继续处理右子树
            self.record += root.val # 处理完右子树后，将当前节点值添加到节点和中
            root.val = self.record  # 将当前节点值改为节点和
            if root.left:           # 处理左子树
                find(root.left)
        if root:
            find(root)
        return root</code></pre></div>
