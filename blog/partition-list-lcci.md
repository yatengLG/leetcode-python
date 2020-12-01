Leetcode 面试题 02.04. 分割链表
<p>编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于&ldquo;右半部分&rdquo;即可，其不需要被置于左右两部分之间。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> head = 3-&gt;5-&gt;8-&gt;5-&gt;10-&gt;2-&gt;1, <em>x</em> = 5

<strong>输出:</strong> 3-&gt;1-&gt;2-&gt;10-&gt;5-&gt;5-&gt;8

</pre>





 **难度**: Medium



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了69.92% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    使用双指针，一个指针遍历，一个指针指向链头。
    若当前节点值小于阈值，则将当前节点挪到链头。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        if not head:
            return head
        while q.next:
            if q.next.val < x:
                r = q.next
                q.next = q.next.next
                r.next = p
                p = r
            else:
                q = q.next
        return p

</code></pre></div>
