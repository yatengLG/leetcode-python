Leetcode 94. 二叉树的中序遍历
<p>给定一个二叉树，返回它的<em>中序&nbsp;</em>遍历。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [1,null,2,3]

   1

    \

     2

    /

   3



<strong>输出:</strong> [1,3,2]</pre>



<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>





 **难度**: Medium



 **标签**: 栈、 树、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了96.63% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了71.27% 的用户

解题思路：
    递归，模拟中序遍历即可
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def find(root): # 当前节点
            if root.left:   # 如果当前节点存在左子树，则遍历左子树
                find(root.left)
            result.append(root.val) # 遍历完左子树后，将当前节点添加到最终结果中
            if root.right:  # 然后遍历右子树
                find(root.right)
        if root:
            find(root)
        return result</code></pre></div>
