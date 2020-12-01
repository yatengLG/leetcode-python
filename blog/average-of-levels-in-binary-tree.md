Leetcode 637. 二叉树的层平均值
<p>给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。</p>


<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>

    3

   / \

  9  20

    /  \

   15   7

<strong>输出：</strong>[3, 14.5, 11]

<strong>解释：</strong>

第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>节点值的范围在32位有符号整数范围内。</li>

</ul>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了94.94% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了56.04% 的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if root == None:
            return result

        record = [root]
        while record:
            vals = [node.val for node in record]
            result.append(sum(vals) / len(vals))
            record_ = []

            for node in record:
                if node.left:
                    record_.append(node.left)

                if node.right:
                    record_.append(node.right)
            record = record_
        return result
</code></pre></div>
