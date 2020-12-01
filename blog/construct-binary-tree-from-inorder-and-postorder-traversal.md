Leetcode 106. 从中序与后序遍历序列构造二叉树
<p>根据一棵树的中序遍历与后序遍历构造二叉树。</p>


<p><strong>注意:</strong><br>

你可以假设树中没有重复的元素。</p>



<p>例如，给出</p>



<pre>中序遍历 inorder =&nbsp;[9,3,15,20,7]

后序遍历 postorder = [9,15,7,20,3]</pre>



<p>返回如下的二叉树：</p>



<pre>    3

   / \

  9  20

    /  \

   15   7

</pre>





 **难度**: Medium



 **标签**: 树、 深度优先搜索、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：192 ms, 在所有 Python3 提交中击败了56.79% 的用户
内存消耗：86.4 MB, 在所有 Python3 提交中击败了5.01% 的用户


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def find(inorder, postorder):
            if inorder == []:
                return
            node = postorder[-1]    # 后续遍历的最后一个为当前树的根
            node_index = inorder.index(node)    # 中序遍历中，根左侧为左子树节点，右侧为右子树节点

            node = TreeNode(node)   # 当前节点
            node.left = find(inorder[:node_index], postorder[:node_index])  # 划分左子树中序及后序
            node.right = find(inorder[node_index+1:], postorder[node_index:-1]) # 划分右子树中序及后序
            return node

        t = find(inorder, postorder)
        return t</code></pre></div>
