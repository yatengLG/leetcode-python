Leetcode 617. 合并二叉树
<p>给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。</p>


<p>你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则<strong>不为&nbsp;</strong>NULL 的节点将直接作为新二叉树的节点。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre>

<strong>输入:</strong> 

	Tree 1                     Tree 2                  

          1                         2                             

         / \                       / \                            

        3   2                     1   3                        

       /                           \   \                      

      5                             4   7                  

<strong>输出:</strong> 

合并后的树:

	     3

	    / \

	   4   5

	  / \   \ 

	 5   4   7

</pre>



<p><strong>注意:</strong>&nbsp;合并必须从两个树的根节点开始。</p>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了64.10% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了79.35% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def find(root1, root2): # 两棵树的对应节点
            if root1 and root2: # 如果节点都存在
                node = TreeNode(root1.val + root2.val)  # 合并后的当前节点为两树节点和
                node.left = find(root1.left, root2.left)    # 处理两树的对应左子树， 返回的节点为当前合并子树的左子树
                node.right = find(root1.right, root2.right) # 处理两树的对应右子树

            elif root1 or root2:    # 只存在一个节点
                node = TreeNode(root1.val if root1 else root2.val)  # 当前节点等于存在节点值
                node.left = find(root1.left if root1 else None, root2.left if root2 else None)  # 遍历存在节点的左子树
                node.right = find(root1.right if root1 else None, root2.right if root2 else None)   # 遍历存在节点的右子树
            else:
                return None # 均不存在返回None
            return node
        t = find(t1, t2)
        return t


"""
执行用时：100 ms, 在所有 Python3 提交中击败了91.61% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了46.33% 的用户

解题思路：
    同上，但不新建树
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def find(root1, root2): # 两棵树的对应节点
            if root1 and root2: # 如果节点都存在
                root1.val = root1.val + root2.val  # 合并后的当前节点为两树节点和
                root1.left = find(root1.left, root2.left)    # 处理两树的对应左子树， 返回的节点为当前合并子树的左子树
                root1.right = find(root1.right, root2.right) # 处理两树的对应右子树

            elif root1 or root2:    # 只存在一个节点, 直接返回存在的节点即可
                return root1 if root1 else root2
            else:
                return None # 均不存在返回None
            return root1
        t = find(t1, t2)
        return t
</code></pre></div>
