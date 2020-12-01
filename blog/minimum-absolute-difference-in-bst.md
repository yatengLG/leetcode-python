Leetcode 530. 二叉搜索树的最小绝对差
<p>给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。</p>


<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>



   1

    \

     3

    /

   2



<strong>输出：</strong>

1



<strong>解释：

</strong>最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>树中至少有 2 个节点。</li>

	<li>本题与 783 <a href="https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/">https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/</a> 相同</li>

</ul>





 **难度**: Easy



 **标签**: 树、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了95.72% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了44.12% 的用户

解题思路：
    中序遍历
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.result = self.val = float('inf')   # 记录最终结果，以及当前节点值
        def find(root):
            if root:
                l = find(root.left)     # 先遍历左子树
                if l:
                    self.result = min(abs(self.val-l.val), self.result) # 判断节点差值绝对值，更新最小值
                    self.val = l.val

                self.result = min(abs(self.val - root.val), self.result)    # 根节点
                self.val = root.val

                r = find(root.right)    # 右子树
                if r:
                    self.result = min(abs(self.val - r.val), self.result)
                    self.val = r.val

        find(root)
        return int(self.result)</code></pre></div>
