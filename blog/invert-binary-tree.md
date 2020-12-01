Leetcode 226. 翻转二叉树
<p>翻转一棵二叉树。</p>


<p><strong>示例：</strong></p>



<p>输入：</p>



<pre>     4

   /   \

  2     7

 / \   / \

1   3 6   9</pre>



<p>输出：</p>



<pre>     4

   /   \

  7     2

 / \   / \

9   6 3   1</pre>



<p><strong>备注:</strong><br>

这个问题是受到 <a href="https://twitter.com/mxcl" target="_blank">Max Howell </a>的 <a href="https://twitter.com/mxcl/status/608682016205344768" target="_blank">原问题</a> 启发的 ：</p>



<blockquote>谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。</blockquote>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.80% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了6.61% 的用户

解题思路：
    递归，翻转二叉树左右子树即可
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root:
                root.left, root.right = root.right, root.left

                invert(root.left)
                invert(root.right)
        invert(root)
        return root</code></pre></div>
