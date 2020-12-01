Leetcode 236. 二叉树的最近公共祖先
<p>给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。</p>


<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。&rdquo;</p>



<p>例如，给定如下二叉树:&nbsp; root =&nbsp;[3,5,1,6,2,0,8,null,null,7,4]</p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/binarytree.png" style="height: 190px; width: 200px;"></p>



<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

<strong>输出:</strong> 3

<strong>解释: </strong>节点 <code>5 </code>和节点 <code>1 </code>的最近公共祖先是节点 <code>3。</code>

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4

<strong>输出:</strong> 5

<strong>解释: </strong>节点 <code>5 </code>和节点 <code>4 </code>的最近公共祖先是节点 <code>5。</code>因为根据定义最近公共祖先节点可以为节点本身。

</pre>



<p>&nbsp;</p>



<p><strong>说明:</strong></p>



<ul>

	<li>所有节点的值都是唯一的。</li>

	<li>p、q 为不同节点且均存在于给定的二叉树中。</li>

</ul>





 **难度**: Medium



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
执行用时：84 ms, 在所有 Python3 提交中击败了85.44% 的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了22.15% 的用户

解题思路：
    存在以下三种情况：
        1. 当前根节点 等于指定节点，则另一个节点肯定存在于当前节点的子树中，当前节点为最近公共祖先
        2. 指定节点分别存在与当前节点的左右子树中，当前节点为最近公共祖先
        3. 若都存在于同侧子树中，下移根节点，在本侧子树中寻找
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if right and left:
            return root
        if right:
            return right
        if left:
            return left

</code></pre></div>
