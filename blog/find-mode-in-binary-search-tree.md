Leetcode 501. 二叉搜索树中的众数
<p>给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。</p>


<p>假定 BST 有如下定义：</p>



<ul>

	<li>结点左子树中所含结点的值小于等于当前结点的值</li>

	<li>结点右子树中所含结点的值大于等于当前结点的值</li>

	<li>左子树和右子树都是二叉搜索树</li>

</ul>



<p>例如：<br>

给定 BST <code>[1,null,2,2]</code>,</p>



<pre>   1

    \

     2

    /

   2

</pre>



<p><code>返回[2]</code>.</p>



<p><strong>提示</strong>：如果众数超过1个，不需考虑输出顺序</p>



<p><strong>进阶：</strong>你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了99.56% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了43.30% 的用户

解题思路：
    具体实现见代码注释
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        record = {}         # 用于保存每个节点出现的次数
        def find(root):     # 递归
            if root:
                if root.val not in record:
                    record[root.val] = 1
                else:
                    record[root.val] += 1
                find(root.left)
                find(root.right)

        find(root)
        result = {} # 各出现次数的节点
        for k, v in record.items():
            if v not in result:
                result[v] = [k]
            else:
                result[v].append(k)
        return result[sorted(result.keys())[-1]]    # 返回出现次数最多的节点
</code></pre></div>
