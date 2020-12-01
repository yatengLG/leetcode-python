Leetcode 83. 删除排序链表中的重复元素
<p>给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> 1-&gt;1-&gt;2

<strong>输出:</strong> 1-&gt;2

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;3

<strong>输出:</strong> 1-&gt;2-&gt;3</pre>





 **难度**: Easy



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了93.86% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了66.25% 的用户

解题思路：
    单指针去重
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next: # 如果未到末尾
            if p.val == p.next.val: # 如果相等，则删掉重复的元素
                p.next = p.next.next
            else:
                p = p.next  # 不重复则移动指针
        return head
</code></pre></div>
