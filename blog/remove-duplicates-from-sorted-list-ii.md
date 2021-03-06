Leetcode 82. 删除排序链表中的重复元素 II
<p>给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中&nbsp;<em>没有重复出现&nbsp;</em>的数字。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;3-&gt;4-&gt;4-&gt;5

<strong>输出:</strong> 1-&gt;2-&gt;5

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> 1-&gt;1-&gt;1-&gt;2-&gt;3

<strong>输出:</strong> 2-&gt;3</pre>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了93.79% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了50.94% 的用户

解题思路：
    双指针
    一个指针指向前面未重复值，一个指向当前遍历值
    用变量repeat记录当前重复值。
    若当前值等于重复值，则删除当前值；若不等于，则查看当前值与其后一值，若相等，更新repeat
    只有当前值不等于repeat时，才尝试更新repeat值
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p, q = ListNode(0, next=head), head
        start = p
        repeat = float('inf')
        while q:
            if (q.val != repeat) and q.next:  # 若当前值不等于repeat，且不是最后一个，尝试更新repeat
                if q.val == q.next.val: # 比较当前值与其后一直，若相等，更新repeat
                    repeat = q.val

            if q.val == repeat: # 若当前值等于repeat
                p.next = q.next # 移动p指针，跳过当前值
                q = p.next
            else:
                p = p.next  # 不等于则同时向后移动p,q
                q = p.next
        return start.next
</code></pre></div>
