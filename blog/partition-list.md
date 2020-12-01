Leetcode 86. 分隔链表
<p>给定一个链表和一个特定值<em> x</em>，对链表进行分隔，使得所有小于 <em>x</em> 的节点都在大于或等于 <em>x</em> 的节点之前。</p>


<p>你应当保留两个分区中每个节点的初始相对位置。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> head = 1-&gt;4-&gt;3-&gt;2-&gt;5-&gt;2, <em>x</em> = 3

<strong>输出:</strong> 1-&gt;2-&gt;2-&gt;4-&gt;3-&gt;5

</pre>





 **难度**: Medium



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了88.07% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了42.98% 的用户

解题思路：
    双指针
    p指针用于记录位置，q指针寻找小于x的节点。
    q指针找到<x的节点后，交换链表
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = ListNode(0, next = head), head   # p指针用于记录位置，q指针用于寻找<x的节点。为便于交换链表，寻找时，均使用指针的next来判断节点
        start = p
        while p and p.next and p.next.val < x:  # 先移动p指针，直到p的下一个节点值大于x
            p = p.next
            q = p.next
        while q and q.next:
            if q.next.val < x:  # 如果q指针指向的下一个节点值小于x, 则交换链表
                p_next = p.next
                q_next_next = q.next.next
                p.next = q.next
                q.next.next = p_next
                q.next = q_next_next
                p = p.next  # 交换链表后，p指针向后移动一位
            else:   # q指针指向的下一个节点值>=x，则移动q指针寻找小于x的节点
                q = q.next

        return start.next</code></pre></div>
