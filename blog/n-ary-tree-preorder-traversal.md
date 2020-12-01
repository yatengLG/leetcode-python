Leetcode 589. N叉树的前序遍历
<p>给定一个 N 叉树，返回其节点值的<em>前序遍历</em>。</p>


<p>例如，给定一个&nbsp;<code>3叉树</code>&nbsp;:</p>



<p>&nbsp;</p>



<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"></p>



<p>&nbsp;</p>



<p>返回其前序遍历: <code>[1,3,5,6,2,4]</code>。</p>



<p>&nbsp;</p>



<p><strong>说明:&nbsp;</strong>递归法很简单，你可以使用迭代法完成此题吗?</p>



 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了86.96% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了85.68% 的用户

解题思路：
    递归
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result =[]
        def find(root):
            if root:
                result.append(root.val)
                childrens = root.children
                for children in childrens:
                    find(children)
        find(root)
        return result</code></pre></div>
