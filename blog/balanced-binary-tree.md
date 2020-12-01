Leetcode 110. 平衡二叉树
<p>给定一个二叉树，判断它是否是高度平衡的二叉树。</p>


<p>本题中，一棵高度平衡二叉树定义为：</p>



<blockquote>

<p>一个二叉树<em>每个节点&nbsp;</em>的左右两个子树的高度差的绝对值不超过1。</p>

</blockquote>



<p><strong>示例 1:</strong></p>



<p>给定二叉树 <code>[3,9,20,null,null,15,7]</code></p>



<pre>    3

   / \

  9  20

    /  \

   15   7</pre>



<p>返回 <code>true</code> 。<br>

<br>

<strong>示例 2:</strong></p>



<p>给定二叉树 <code>[1,2,2,3,3,null,null,4,4]</code></p>



<pre>       1

      / \

     2   2

    / \

   3   3

  / \

 4   4

</pre>



<p>返回&nbsp;<code>false</code> 。</p>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了92.70% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了44.80% 的用户

解题思路：
    递归
    在实现时，参考了官方提供的思路。
    从叶节点开始，一直向上进行判断。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:    # 叶节点，高度为0
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height)>1:    # -1 来表示 子树高度大于1 的情况
                return -1
            else:
                return max(left_height, right_height) + 1   # 如果平衡，则该节点的root高度为 叶节点最大高度+1

        return height(root)>=0
</code></pre></div>
