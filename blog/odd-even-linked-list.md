Leetcode 328. 奇偶链表
<p>给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。</p>


<p>请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL

<strong>输出:</strong> 1-&gt;3-&gt;5-&gt;2-&gt;4-&gt;NULL

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> 2-&gt;1-&gt;3-&gt;5-&gt;6-&gt;4-&gt;7-&gt;NULL 

<strong>输出:</strong> 2-&gt;3-&gt;6-&gt;7-&gt;1-&gt;5-&gt;4-&gt;NULL</pre>



<p><strong>说明:</strong></p>



<ul>

	<li>应当保持奇数节点和偶数节点的相对顺序。</li>

	<li>链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。</li>

</ul>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了99.25% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.20% 的用户

解题思路：
    双指针
    具体实现见代码注释
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not (head and head.next and head.next.next):
            return head

        p, q = head, head.next  # 双指针，p指向插入处，q指向待插入节点前一个

        while q and q.next:
            node = q.next       # 取出node
            q.next = node.next  # 删掉node，连接删后的链表

            p_next = p.next     # 记录p的下一个节点
            p.next = node       # 插入node
            node.next = p_next  # 连接链表

            p = p.next  # 移动指针
            q = q.next
        return head
</code></pre></div>
