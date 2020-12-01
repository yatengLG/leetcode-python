Leetcode 129. 求根到叶子节点数字之和
<p>给定一个二叉树，它的每个结点都存放一个&nbsp;<code>0-9</code>&nbsp;的数字，每条从根到叶子节点的路径都代表一个数字。</p>


<p>例如，从根到叶子节点路径 <code>1-&gt;2-&gt;3</code> 代表数字 <code>123</code>。</p>



<p>计算从根到叶子节点生成的所有数字之和。</p>



<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [1,2,3]

    1

   / \

  2   3

<strong>输出:</strong> 25

<strong>解释:</strong>

从根到叶子节点路径 <code>1-&gt;2</code> 代表数字 <code>12</code>.

从根到叶子节点路径 <code>1-&gt;3</code> 代表数字 <code>13</code>.

因此，数字总和 = 12 + 13 = <code>25</code>.</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [4,9,0,5,1]

    4

   / \

  9   0

&nbsp;/ \

5   1

<strong>输出:</strong> 1026

<strong>解释:</strong>

从根到叶子节点路径 <code>4-&gt;9-&gt;5</code> 代表数字 495.

从根到叶子节点路径 <code>4-&gt;9-&gt;1</code> 代表数字 491.

从根到叶子节点路径 <code>4-&gt;0</code> 代表数字 40.

因此，数字总和 = 495 + 491 + 40 = <code>1026</code>.</pre>





 **难度**: Medium



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了81.35% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    递归，获得每条支线节点组成的数字，然后相加
"""
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        record = []

        def find(root, current):
            current += str(root.val)
            if root.left == None and root.right == None:
                record.append(int(current))
                return
            else:
                if root.left:
                    find(root.left, current)
                if root.right:
                    find(root.right, current)

        if root:
            find(root, '')

        return sum(record)</code></pre></div>
