Leetcode 145. 二叉树的后序遍历
<p>给定一个二叉树，返回它的 <em>后序&nbsp;</em>遍历。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [1,null,2,3]  

   1

    \

     2

    /

   3 



<strong>输出:</strong> [3,2,1]</pre>



<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>





 **难度**: Medium



 **标签**: 栈、 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.79% 的用户
内存消耗：13.2 MB, 在所有 Python3 提交中击败了94.96% 的用户

解题思路：
    递归
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def find(root):
            if root:
                find(root.left) # 先处理左节点
                find(root.right)    # 再处理右节点
                result.append(root.val) # 最后处理当前节点
        find(root)
        return result</code></pre></div>
