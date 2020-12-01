Leetcode 111. 二叉树的最小深度
<p>给定一个二叉树，找出其最小深度。</p>


<p>最小深度是从根节点到最近叶子节点的最短路径上的节点数量。</p>



<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>



<p><strong>示例:</strong></p>



<p>给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>



<pre>    3

   / \

  9  20

    /  \

   15   7</pre>



<p>返回它的最小深度 &nbsp;2.</p>





 **难度**: Easy



 **标签**: 树、 深度优先搜索、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了95.56% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了99.94% 的用户

解题思路：
    广度优先。
    具体实现见代码注释
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        roots = [root]  # 用于保存当前需要 查看的节点， 以根作为起始
        depth = 1       # 用于保存树的最小高度
        while roots:
            roots_c = []
            for r in roots:
                if r != None:   # 如果当前节点 为None，跳过，查看下一个节点
                    if r.left == None and r.right == None:  # 如果当前节点 左子树与右子树均为None, 则当前节点为叶节点，直接返回高度即可
                        return depth
                    else:       # 左右子树存在一个或多个，不是叶节点，则准备查看其左右子树
                        roots_c.append(r.left)
                        roots_c.append(r.right)
            roots = roots_c
            depth += 1  # 遍历完一次后，高度+1
</code></pre></div>
