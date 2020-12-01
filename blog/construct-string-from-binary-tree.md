Leetcode 606. 根据二叉树创建字符串
<p>你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。</p>


<p>空节点则用一对空括号 &quot;()&quot; 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。</p>



<p><strong>示例 1:</strong></p>



<pre>

<strong>输入:</strong> 二叉树: [1,2,3,4]

       1

     /   \

    2     3

   /    

  4     



<strong>输出:</strong> &quot;1(2(4))(3)&quot;



<strong>解释:</strong> 原本将是&ldquo;1(2(4)())(3())&rdquo;，

在你省略所有不必要的空括号对之后，

它将是&ldquo;1(2(4))(3)&rdquo;。

</pre>



<p><strong>示例 2:</strong></p>



<pre>

<strong>输入:</strong> 二叉树: [1,2,3,null,4]

       1

     /   \

    2     3

     \  

      4 



<strong>输出:</strong> &quot;1(2()(4))(3)&quot;



<strong>解释:</strong> 和第一个示例相似，

除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

</pre>





 **难度**: Easy



 **标签**: 树、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了75.57% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了50.00% 的用户

解题思路：
    使用递归处理
    对于左节点有三种情况：存在，则返回节点值；若不存在，但右节点存在，则返回（）；若右节点也不存在，则返回“”
    对于右节点有两种情况：存在，则返回节点值；不存在，则返回“”
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if t.right:
            right = "({})".format(self.tree2str(t.right))
        else:
            right = ""

        if t.left:
            left = "({})".format(self.tree2str(t.left))
        else:
            if t.right:
                left = "()"
            else:
                left = ""
        return str(t.val)+left+ right
</code></pre></div>
