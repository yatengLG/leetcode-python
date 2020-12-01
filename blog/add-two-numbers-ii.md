Leetcode 445. 两数相加 II
<p>给你两个 <strong>非空 </strong>链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。</p>


<p>你可以假设除了数字 0 之外，这两个数字都不会以零开头。</p>



<p>&nbsp;</p>



<p><strong>进阶：</strong></p>



<p>如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。</p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>(7 -&gt; 2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)

<strong>输出：</strong>7 -&gt; 8 -&gt; 0 -&gt; 7

</pre>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.43% 的用户

解题思路：
    先找到长链表比短链表 前部分多出的位置。
    将多出的位，直接添加到最终结果中，然后将对应位的值相加作为当前节点的值
    然后处理递归进位
    最终，判断首位是否进位
    具体实现见代码注释
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2   # p,q 指针分别指向两个链表
        while p and q:  # 找出一个长链表比短链表长出的部分
            p = p.next
            q = q.next
        if p:           # 如果p 指针剩余， 则l1长l2短， 初始化pl,ps指针，分别指向长短链表
            pl, ps = l1, l2
            p = p
        else:
            pl, ps = l2, l1
            p = q

        result = ListNode(0)    # 用于记录最终结果
        r = result  # 最终结果指针
        while p:    # 走完长链表剩余没走完的部分，pl找到长链表前半部分多出的部位，直接添加到result中
            r.next = pl
            r = r.next

            pl = pl.next
            p = p.next

        while pl and ps:    # 走的剩余部分相同时，同时移动pl,ps， 计算对应节点值的和
            pl.val += ps.val
            r.next = pl
            r = r.next

            pl = pl.next    # 同时移动pl,ps
            ps = ps.next

        def carry(node):    # 递归处理进位
            if node.next:
                node_next = carry(node.next)    # 如果当前节点下一位存在，继续遍历
                c = node_next.val // 10         # 计算进位
                node.val = node.val + c         # 当前节点值 = 当前节点值 + 下一位的进位
                node_next.val = node_next.val % 10  # 更新下一位的值

            return node

        node = carry(result)

        if node.val > 0:    # 处理首位是否进位
            return node
        else:
            return node.next
</code></pre></div>
