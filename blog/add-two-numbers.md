Leetcode 2. 两数相加
<p>给出两个&nbsp;<strong>非空</strong> 的链表用来表示两个非负的整数。其中，它们各自的位数是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且它们的每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>


<p>如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。</p>



<p>您可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>(2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)

<strong>输出：</strong>7 -&gt; 0 -&gt; 8

<strong>原因：</strong>342 + 465 = 807

</pre>





 **难度**: Medium



 **标签**: 链表、 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了82.51% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.13%

解题思路：
    依次计算当前位和，并记录进位
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        l3 = l4 = ListNode(0)
        while l1 or l2 or add:
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            l3.next = ListNode(add % 10)
            add = add // 10
            l3 = l3.next
        return l4.next


</code></pre></div>
