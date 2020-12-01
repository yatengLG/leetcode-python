Leetcode 235. 二叉搜索树的最近公共祖先
<p>给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。</p>


<p><a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。&rdquo;</p>



<p>例如，给定如下二叉搜索树:&nbsp; root =&nbsp;[6,2,8,0,4,7,9,null,null,3,5]</p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png" style="height: 190px; width: 200px;"></p>



<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

<strong>输出:</strong> 6 

<strong>解释: </strong>节点 <code>2 </code>和节点 <code>8 </code>的最近公共祖先是 <code>6。</code>

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4

<strong>输出:</strong> 2

<strong>解释: </strong>节点 <code>2</code> 和节点 <code>4</code> 的最近公共祖先是 <code>2</code>, 因为根据定义最近公共祖先节点可以为节点本身。</pre>



<p>&nbsp;</p>



<p><strong>说明:</strong></p>



<ul>

	<li>所有节点的值都是唯一的。</li>

	<li>p、q 为不同节点且均存在于给定的二叉搜索树中。</li>

</ul>





 **难度**: Easy



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
执行用时：80 ms, 在所有 Python3 提交中击败了99.61% 的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了86.69% 的用户

解题思路：
    因为是二叉搜索树，左节点值必定小于右节点。
    如果当前节点值处于俩个指定节点之间，则最近公共祖先必定为当前节点。
    若不是，通过比较节点值，对树进行更新
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l_val, r_val = p.val, q.val
        if l_val > r_val:       # 确保指定节点值大小顺序
            l_val, r_val = r_val, l_val

        while True:
            if l_val <= root.val <= r_val:  # 当前节点处于指定两节点之间
                return root

            if root.val > r_val:    # 当前节点小于指定节点最小值，更新当前节点为节点左子树
                root = root.left
            if root.val < l_val:    #
                root = root.right


"""
执行用时：88 ms, 在所有 Python3 提交中击败了95.71% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了97.46% 的用户

解题思路：
    递归
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        def find(root, p, q):
            if p.val <= root.val <= q.val:  # 比较当前节点与p,q的值， 如果处于p,q之间，则返回
                return root
            elif root.val < p.val:  # 如果当前节点值小于p,则遍历右子树
                return find(root.right, p, q)
            else:   # 否则，遍历左子树
                return find(root.left, p, q)
        return find(root, p, q)</code></pre></div>
