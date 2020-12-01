Leetcode 116. 填充每个节点的下一个右侧节点指针
<p>给定一个<strong>完美二叉树</strong>，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：</p>


<pre>struct Node {

  int val;

  Node *left;

  Node *right;

  Node *next;

}</pre>



<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 <code>NULL</code>。</p>



<p>初始状态下，所有&nbsp;next 指针都被设置为 <code>NULL</code>。</p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png" style="height: 218px; width: 640px;"></p>



<pre><strong>输入：</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;left&quot;:{&quot;$id&quot;:&quot;2&quot;,&quot;left&quot;:{&quot;$id&quot;:&quot;3&quot;,&quot;left&quot;:null,&quot;next&quot;:null,&quot;right&quot;:null,&quot;val&quot;:4},&quot;next&quot;:null,&quot;right&quot;:{&quot;$id&quot;:&quot;4&quot;,&quot;left&quot;:null,&quot;next&quot;:null,&quot;right&quot;:null,&quot;val&quot;:5},&quot;val&quot;:2},&quot;next&quot;:null,&quot;right&quot;:{&quot;$id&quot;:&quot;5&quot;,&quot;left&quot;:{&quot;$id&quot;:&quot;6&quot;,&quot;left&quot;:null,&quot;next&quot;:null,&quot;right&quot;:null,&quot;val&quot;:6},&quot;next&quot;:null,&quot;right&quot;:{&quot;$id&quot;:&quot;7&quot;,&quot;left&quot;:null,&quot;next&quot;:null,&quot;right&quot;:null,&quot;val&quot;:7},&quot;val&quot;:3},&quot;val&quot;:1}



<strong>输出：</strong>{&quot;$id&quot;:&quot;1&quot;,&quot;left&quot;:{&quot;$id&quot;:&quot;2&quot;,&quot;left&quot;:{&quot;$id&quot;:&quot;3&quot;,&quot;left&quot;:null,&quot;next&quot;:{&quot;$id&quot;:&quot;4&quot;,&quot;left&quot;:null,&quot;next&quot;:{&quot;$id&quot;:&quot;5&quot;,&quot;left&quot;:null,&quot;next&quot;:{&quot;$id&quot;:&quot;6&quot;,&quot;left&quot;:null,&quot;next&quot;:null,&quot;right&quot;:null,&quot;val&quot;:7},&quot;right&quot;:null,&quot;val&quot;:6},&quot;right&quot;:null,&quot;val&quot;:5},&quot;right&quot;:null,&quot;val&quot;:4},&quot;next&quot;:{&quot;$id&quot;:&quot;7&quot;,&quot;left&quot;:{&quot;$ref&quot;:&quot;5&quot;},&quot;next&quot;:null,&quot;right&quot;:{&quot;$ref&quot;:&quot;6&quot;},&quot;val&quot;:3},&quot;right&quot;:{&quot;$ref&quot;:&quot;4&quot;},&quot;val&quot;:2},&quot;next&quot;:null,&quot;right&quot;:{&quot;$ref&quot;:&quot;7&quot;},&quot;val&quot;:1}



<strong>解释：</strong>给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>你只能使用常量级额外空间。</li>

	<li>使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。</li>

</ul>





 **难度**: Medium



 **标签**: 树、 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：76 ms, 在所有 Python3 提交中击败了85.75% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.31% 的用户

解题思路：
    将树中节点，以每层存入字典中。
    然后读取每层的节点，添加next指针
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        record = {} # 用于记录每层的节点

        def find(root, h):  # 递归遍历树，以高度从左到右将节点存入字典
            if root:
                if h in record:
                    record[h].append(root)
                else:
                    record[h] = [root]
                find(root.left, h+1)
                find(root.right, h+1)

        find(root, 0)
        for h, roots in record.items(): # 读取保存的字典，一层一层处理节点
            roots += [None]
            for i, r in enumerate(roots):
                if r:
                    r.next = roots[i+1]
        return root
</code></pre></div>
