Leetcode 104. 二叉树的最大深度
<p>给定一个二叉树，找出其最大深度。</p>


<p>二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。</p>



<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>



<p><strong>示例：</strong><br>

给定二叉树 <code>[3,9,20,null,null,15,7]</code>，</p>



<pre>    3

   / \

  9  20

    /  \

   15   7</pre>



<p>返回它的最大深度&nbsp;3 。</p>





 **难度**: Easy



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了90.78% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了9.95% 的用户

解题思路：
    递归
    具体详情见代码注释
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.d = 0
        def find(root, d):
            if root:    # 如果当前节点不为None，深度+1
                d += 1
                find(root.left, d)  # 处理左子树
                find(root.right, d) # 处理右子树
            else:   # 到叶节点时，更新深度
                if self.d < d:
                    self.d = d
        find(root, 0)
        return self.d
</code></pre></div>
