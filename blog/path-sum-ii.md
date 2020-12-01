Leetcode 113. 路径总和 II
<p>给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。</p>


<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>



<p><strong>示例:</strong><br>

给定如下二叉树，以及目标和&nbsp;<code>sum = 22</code>，</p>



<pre>              <strong>5</strong>

             / \

            <strong>4</strong>   <strong>8</strong>

           /   / \

          <strong>11</strong>  13  <strong>4</strong>

         /  \    / \

        7    <strong>2</strong>  <strong>5</strong>   1

</pre>



<p>返回:</p>



<pre>[

   [5,4,11,2],

   [5,8,4,5]

]

</pre>





 **难度**: Medium



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了62.60% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了25.28% 的用户

解题思路：
    回溯
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        def find(root, current, target):
            if root.left == None and root.right == None and target == root.val:
                result.append(current[:] + [root.val])
                return
            if root.left:
                find(root.left, current + [root.val], target - root.val)  # 回溯
            if root.right:
                find(root.right, current + [root.val], target - root.val)

        if root:
            find(root, [], sum)
        return result</code></pre></div>
