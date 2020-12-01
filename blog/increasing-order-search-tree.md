Leetcode 897. 递增顺序查找树
<p>给你一个树，请你 <strong>按中序遍历</strong> 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。</p>


<p>&nbsp;</p>



<p><strong>示例 ：</strong></p>



<pre><strong>输入：</strong>[5,3,6,2,4,null,8,1,null,null,null,7,9]



       5

      / \

    3    6

   / \    \

  2   4    8

&nbsp;/        / \ 

1        7   9



<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]



 1

&nbsp; \

&nbsp;  2

&nbsp;   \

&nbsp;    3

&nbsp;     \

&nbsp;      4

&nbsp;       \

&nbsp;        5

&nbsp;         \

&nbsp;          6

&nbsp;           \

&nbsp;            7

&nbsp;             \

&nbsp;              8

&nbsp;               \

                 9  </pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li>给定树中的结点数介于 <code>1</code> 和&nbsp;<code>100</code> 之间。</li>

	<li>每个结点都有一个从 <code>0</code> 到 <code>1000</code> 范围内的唯一整数值。</li>

</ol>





 **难度**: Easy



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：24 ms, 在所有 Python3 提交中击败了99.87% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了65.60% 的用户

解题思路：
    递归
    先中序遍历，然后组成数
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def find(root):
            if root:

                find(root.left)
                result.append(root.val)
                find(root.right)
        find(root)
        # 建树
        start = now = TreeNode(0)
        for r in result:
            now.right = TreeNode(r)
            now = now.right

        return start.right
</code></pre></div>
