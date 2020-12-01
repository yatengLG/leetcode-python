Leetcode 107. 二叉树的层次遍历 II
<p>给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）</p>


<p>例如：<br>

给定二叉树 <code>[3,9,20,null,null,15,7]</code>,</p>



<pre>    3

   / \

  9  20

    /  \

   15   7

</pre>



<p>返回其自底向上的层次遍历为：</p>



<pre>[

  [15,7],

  [9,20],

  [3]

]

</pre>





 **难度**: Easy



 **标签**: 树、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了78.88% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了14.82% 的用户

解题思路：
    深度优先遍历
    并记录当前层数，便于结果存储

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res)<depth+1:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        return res[::-1]
</code></pre></div>
