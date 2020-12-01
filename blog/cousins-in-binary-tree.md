Leetcode 993. 二叉树的堂兄弟节点
<p>在二叉树中，根节点位于深度 <code>0</code> 处，每个深度为 <code>k</code> 的节点的子节点位于深度 <code>k+1</code> 处。</p>


<p>如果二叉树的两个节点深度相同，但<strong>父节点不同</strong>，则它们是一对<em>堂兄弟节点</em>。</p>



<p>我们给出了具有唯一值的二叉树的根节点 <code>root</code>，以及树中两个不同节点的值 <code>x</code> 和 <code>y</code>。</p>



<p>只有与值 <code>x</code> 和 <code>y</code> 对应的节点是堂兄弟节点时，才返回 <code>true</code>。否则，返回 <code>false</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：<br>

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png" style="height: 160px; width: 180px;"></strong></p>



<pre><strong>输入：</strong>root = [1,2,3,4], x = 4, y = 3

<strong>输出：</strong>false

</pre>



<p><strong>示例 2：<br>

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png" style="height: 160px; width: 201px;"></strong></p>



<pre><strong>输入：</strong>root = [1,2,3,null,4,null,5], x = 5, y = 4

<strong>输出：</strong>true

</pre>



<p><strong>示例 3：</strong></p>



<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png" style="height: 160px; width: 156px;"></strong></p>



<pre><strong>输入：</strong>root = [1,2,3,null,4], x = 2, y = 3

<strong>输出：</strong>false</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li>二叉树的节点数介于&nbsp;<code>2</code> 到&nbsp;<code>100</code>&nbsp;之间。</li>

	<li>每个节点的值都是唯一的、范围为&nbsp;<code>1</code> 到&nbsp;<code>100</code>&nbsp;的整数。</li>

</ol>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 树、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了95.78% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了17.49% 的用户

解题思路：
    先寻找两节点在树中的位置
    保存，节点的深度和父节点
    具体实现见代码注释
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        record = {} # 用于保存  x,y在树中的深度和父节点
        def find(root, f, h):
            if root:
                if root.val == x or root.val == y:  # 找到x,y
                    record[root.val] = [f, h]       # 记录x,y的父节点和深度
                    return
                find(root.left, root, h+1)
                find(root.right, root, h+1)

        find(root, None, 0)

        if len(record) == 2:    # 如果x,y都找到
            if record[x][1] == record[y][1] and record[x][0] != record[y][0]:   # xy处于同深度，且父节点不同时，返回true
                return True
            else:
                return False
        else:
            return False
</code></pre></div>
