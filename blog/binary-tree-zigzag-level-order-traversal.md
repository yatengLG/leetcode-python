Leetcode 103. 二叉树的锯齿形层次遍历
<p>给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。</p>


<p>例如：<br>

给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>



<pre>    3

   / \

  9  20

    /  \

   15   7

</pre>



<p>返回锯齿形层次遍历如下：</p>



<pre>[

  [3],

  [20,9],

  [15,7]

]

</pre>





 **难度**: Medium



 **标签**: 栈、 树、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了91.91% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.59% 的用户

解题思路：
    深度优先搜索
    然后进行翻转
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        record = {}

        def dfs(root, d):   # 深度优先，使用字典记录每层的节点值
            if root:
                if d in record:
                    record[d].append(root.val)
                else:
                    record[d] = [root.val]
                dfs(root.left, d + 1)
                dfs(root.right, d + 1)

        dfs(root, 0)

        result = []
        reverse = False
        for d in range(len(record)):    # 隔一层翻转一次
            if reverse:
                result.append(record[d][::-1])
            else:
                result.append(record[d])
            reverse = not reverse
        return result</code></pre></div>
