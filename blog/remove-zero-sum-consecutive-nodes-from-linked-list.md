Leetcode 1171. 从链表中删去总和值为零的连续节点
<p>给你一个链表的头节点&nbsp;<code>head</code>，请你编写代码，反复删去链表中由 <strong>总和</strong>&nbsp;值为 <code>0</code> 的连续节点组成的序列，直到不存在这样的序列为止。</p>


<p>删除完毕后，请你返回最终结果链表的头节点。</p>



<p>&nbsp;</p>



<p>你可以返回任何满足题目要求的答案。</p>



<p>（注意，下面示例中的所有序列，都是对&nbsp;<code>ListNode</code>&nbsp;对象序列化的表示。）</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>head = [1,2,-3,3,1]

<strong>输出：</strong>[3,1]

<strong>提示：</strong>答案 [1,2,1] 也是正确的。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>head = [1,2,3,-3,4]

<strong>输出：</strong>[1,2,4]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>head = [1,2,3,-3,-2]

<strong>输出：</strong>[1]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>给你的链表中可能有 <code>1</code> 到&nbsp;<code>1000</code>&nbsp;个节点。</li>

	<li>对于链表中的每个节点，节点的值：<code>-1000 &lt;= node.val &lt;= 1000</code>.</li>

</ul>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了95.06% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了5.35% 的用户

解题思路：
    i~j 和为0， 则必然 sum(0~i) == sum(0~j)
    且，每次删除后，需要重新从头计算，不然会出现中间删去部分又重复删去导致结果错误的情况
        [1, 3, 2, -3, -2, 5, 5, -5, 1]
      0  1  4  6   3   1  6  11  6  7
"""
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        start = ListNode(0, next=head)
        record = {0: start}
        add = 0
        while head:
            add += head.val
            if add in record:
                record[add].next = head.next    # 删除子链表
                return self.removeZeroSumSublists(start.next)   # 删去一个子链表后，重新计算
            else:
                record[add] = head
                head = head.next
        return start.next
</code></pre></div>
