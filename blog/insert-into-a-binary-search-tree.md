Leetcode 701. 二叉搜索树中的插入操作
<p>给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。</p>


<p>注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。</p>



<p>&nbsp;</p>



<p>例如,&nbsp;</p>



<pre>给定二叉搜索树:



        4

       / \

      2   7

     / \

    1   3



和 插入的值: 5

</pre>



<p>你可以返回这个二叉搜索树:</p>



<pre>         4

       /   \

      2     7

     / \   /

    1   3 5

</pre>



<p>或者这个树也是有效的:</p>



<pre>         5

       /   \

      2     7

     / \   

    1   3

         \

          4

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>给定的树上的节点数介于 <code>0</code> 和 <code>10^4</code> 之间</li>

	<li>每个节点都有一个唯一整数值，取值范围从 <code>0</code> 到 <code>10^8</code></li>

	<li><code>-10^8 &lt;= val &lt;= 10^8</code></li>

	<li>新值和原始二叉搜索树中的任意节点值都不同</li>

</ul>





 **难度**: Medium



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：164 ms, 在所有 Python3 提交中击败了73.44% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了81.96% 的用户

解题思路：
    在叶节点插入插入点
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        insert_node = TreeNode(val) # 待插入的节点
        def find(root):
            if root.val < val:  # 如果当前节点值小于插入值，遍历右子树
                if root.right:  # 如果右子树存在，遍历右子树
                    find(root.right)
                else:   # 如果不存在右子树，当前节点右节点为插入节点
                    root.right = insert_node
            else:   # 左子树同处理
                if root.left:
                    find(root.left)
                else:
                    root.left = insert_node
        if root:    # 如果树不为空， 开始遍历，插入插入节点点
            find(root)
            return root
        else:   # 如果当前树为空，则直接返回待插入节点
            return insert_node</code></pre></div>
