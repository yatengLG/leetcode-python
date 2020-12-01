Leetcode 147. 对链表进行插入排序
<p>对链表进行插入排序。</p>


<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif"><br>

<small>插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。<br>

每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。</small></p>



<p>&nbsp;</p>



<p><strong>插入排序算法：</strong></p>



<ol>

	<li>插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。</li>

	<li>每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。</li>

	<li>重复直到所有输入数据插入完为止。</li>

</ol>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入:</strong> 4-&gt;2-&gt;1-&gt;3

<strong>输出:</strong> 1-&gt;2-&gt;3-&gt;4

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入:</strong> -1-&gt;5-&gt;3-&gt;4-&gt;0

<strong>输出:</strong> -1-&gt;0-&gt;3-&gt;4-&gt;5

</pre>





 **难度**: Medium



 **标签**: 排序、 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：160 ms, 在所有 Python3 提交中击败了94.60% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了7.93% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        result = ListNode(float('-inf'), next=head)
        r = result  # 指针r.next指向当前节点
        while r.next:   # 当前节点不为None时，
            if r.next.val > r.val:  # 如果当前节点后一个节点大于当前节点值，后移指针，处理下一个
                r = r.next
            else:   # 小于时，执行插入操作
                node = r.next   # 记录并删除当前节点node
                p = result
                r.next = r.next.next
                while p.next.val < node.val:    # 在排序好的链表中，寻找插入node的位置
                    p = p.next
                node.next = p.next  # 插入节点
                p.next = node
        return result.next
</code></pre></div>
