Leetcode 142. 环形链表 II
<p>给定一个链表，返回链表开始入环的第一个节点。&nbsp;如果链表无环，则返回&nbsp;<code>null</code>。</p>


<p>为了表示给定链表中的环，我们使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 <code>pos</code> 是 <code>-1</code>，则在该链表中没有环。</p>



<p><strong>说明：</strong>不允许修改给定的链表。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>head = [3,2,0,-4], pos = 1

<strong>输出：</strong>tail connects to node index 1

<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。

</pre>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" style="height: 97px; width: 300px;"></p>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入：</strong>head = [1,2], pos = 0

<strong>输出：</strong>tail connects to node index 0

<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。

</pre>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 74px; width: 141px;"></p>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>head = [1], pos = -1

<strong>输出：</strong>no cycle

<strong>解释：</strong>链表中没有环。

</pre>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 45px; width: 45px;"></p>



<p>&nbsp;</p>



<p><strong>进阶：</strong><br>

你是否可以不用额外空间解决此题？</p>





 **难度**: Medium



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了98.32% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了74.63% 的用户

解题思路：
    快慢指针

    |<----    l1   ---->|< --------
    1   2   3   4   5   6   7   8   l2
                        15      9   ↓
                        14      10  __
                        13  12  11

    从头部到入环 距离为 l1， 入环到快慢指针相遇点为l2， 环长 c

    则， 慢指针走过的距离为 s = 1 + l1 + l2
        快指针走过的距离为 f = l1 + l2 + nc  绕了环内走了n圈

    2s = f
    则，  2 + 2l1 + 2l2 = l1 + l2 + nc

    所求入环处 l1 = nc - l2 - 2
    nc - l2 可由 慢指针从相遇处 开始绕环走到入环处得来。
    即 在相遇时，从起点前两个距离开始，初始化一个指针， 同时慢指针从相遇处继续走。 新指针与慢指针会在入环处相遇
"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s, f = ListNode(0, next= head), head    # 快慢指针

        while s != f:   # 相遇则有环，且当前位置为相遇处
            if f and f.next:
                s = s.next
                f = f.next.next
            else:   # 无环
                return
        # 有环时，初始化一个新指针，在开始前两个距离处
        new = ListNode(0, next=ListNode(0, next = head))    # 新指针

        while new != s: # 新指针与慢指针同时走，相遇处便是入环点
            new = new.next
            s = s.next

        return s</code></pre></div>
