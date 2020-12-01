Leetcode 剑指 Offer 32 - II. 从上到下打印二叉树 II
<p>从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。</p>


<p>&nbsp;</p>



<p>例如:<br>

给定二叉树:&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>



<pre>    3

   / \

  9  20

    /  \

   15   7

</pre>



<p>返回其层次遍历结果：</p>



<pre>[

  [3],

  [9,20],

  [15,7]

]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>节点总数 &lt;= 1000</code></li>

</ol>



<p>注意：本题与主站 102 题相同：<a href="https://leetcode-cn.com/problems/binary-tree-level-order-traversal/">https://leetcode-cn.com/problems/binary-tree-level-order-traversal/</a></p>





 **难度**: Easy



 **标签**: 树、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了84.24% 的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了5.03%

解题思路：
    递归
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        def find(root, deep):   # 使用deep记录当前深度
            if root:
                if deep > len(result)-1:
                    result.append([])
                result[deep].append(root.val)   # 添加到最终结果的对应深度列表中
                find(root.left, deep+1)     # 处理左子树
                find(root.right, deep+1)    # 右子树
        find(root, 0)
        return result</code></pre></div>
