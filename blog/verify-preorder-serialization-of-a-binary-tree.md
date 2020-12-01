Leetcode 331. 验证二叉树的前序序列化
<p>序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 <code>#</code>。</p>


<pre>     _9_

    /   \

   3     2

  / \   / \

 4   1  #  6

/ \ / \   / \

# # # #   # #

</pre>



<p>例如，上面的二叉树可以被序列化为字符串 <code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>，其中 <code>#</code> 代表一个空节点。</p>



<p>给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。</p>



<p>每个以逗号分隔的字符或为一个整数或为一个表示 <code>null</code> 指针的 <code>&#39;#&#39;</code> 。</p>



<p>你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如&nbsp;<code>&quot;1,,3&quot;</code> 。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入: </strong><code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>

<strong>输出: </strong><code>true</code></pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入: </strong><code>&quot;1,#&quot;</code>

<strong>输出: </strong><code>false</code>

</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入: </strong><code>&quot;9,#,#,1&quot;</code>

<strong>输出: </strong><code>false</code></pre>





 **难度**: Medium



 **标签**: 栈、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了42.51% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了5.11% 的用户

解题思路：
    栈
    每次删除最后一个节点，剩余的序列仍构成树
    每删除一个非None节点，均会删除其子树，也就是两个None节点。
    删除一个非None节点后，会使其根，添加一个None节点。
    具体实现见代码注释
"""
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        record = []
        for p in preorder.split(','):
            record.append(p)

        def pop_node(stack):    # 删除当前树序列中最右侧的非None节点
            if len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#':   # 非None节点必然存在两个None节点;只存在根节点，其序列也必然>=3
                stack.pop() # 首先删除两个None节点
                stack.pop()
                n = 1   # 统计后续需要补入序列的# None节点
                for p in stack[::-1]:   # 倒叙从序列中寻找非None节点，如果是None节点，先出栈，并计入n中
                    if p == '#':
                        n += 1
                        stack.pop()
                    else:   # 找到非None节点，跳出循环
                        break
                if stack:
                    stack.pop() # 删除非None节点
                    stack += ['#'] * n  # 将n个None 填入序列中
                    if pop_node(stack): # 继续递归删除当前树中的最右侧非None节点
                        return True
                    else:
                        return False
                else:
                    return False
            elif stack == ['#']:    # 如果当前树 len<3， 且为None，则说明所有节点均可删除，原序列构成树，返回True
                return True
            else:
                return False

        return pop_node(record)
</code></pre></div>
