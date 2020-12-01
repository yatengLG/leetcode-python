Leetcode 面试题 02.05. 链表求和
<p>给定两个用链表表示的整数，每个节点包含一个数位。</p>
<p>这些数位是反向存放的，也就是个位排在链表首部。</p>

<p>编写函数对这两个整数求和，并用链表形式返回结果。</p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre>

<strong>输入：</strong>(7 -&gt; 1 -&gt; 6) + (5 -&gt; 9 -&gt; 2)，即617 + 295

<strong>输出：</strong>2 -&gt; 1 -&gt; 9，即912

</pre>



<p><strong>进阶：</strong>假设这些数位是正向存放的，请再做一遍。</p>



<p><strong>示例：</strong></p>



<pre>

<strong>输入：</strong>(6 -&gt; 1 -&gt; 7) + (2 -&gt; 9 -&gt; 5)，即617 + 295

<strong>输出：</strong>9 -&gt; 1 -&gt; 2，即912

</pre>





 **难度**: Medium



 **标签**: 链表、 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：76 ms, 在所有 Python3 提交中击败了61.41% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    使用双指针分别遍历两个链表，使用一个数记录进位。
    若双指针与进位均空时，结束。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        head = o = ListNode(0)
        add = 0

        while (p or q or add):

            if p:
                add = p.val + add
                p = p.next
            if q:
                add = q.val + add
                q = q.next
            o.next = ListNode((add % 10))
            o = o.next
            add = add // 10

        return head.next</code></pre></div>
