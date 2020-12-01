Leetcode 24. 两两交换链表中的节点
<p>给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。</p>


<p><strong>你不能只是单纯的改变节点内部的值</strong>，而是需要实际的进行节点交换。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre>给定 <code>1-&gt;2-&gt;3-&gt;4</code>, 你应该返回 <code>2-&gt;1-&gt;4-&gt;3</code>.

</pre>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了97.79% 的用户
内存消耗：13.2 MB, 在所有 Python3 提交中击败了94.82% 的用户

解题思路：
    新建一个链表
    通过指针p，向新建链表中添加节点。
    需要注意尾部的处理
    详见代码注释
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        result = ListNode(0, next=None) # 新建链表
        r = result  # 新建链表指针
        p = head    # 原链表指针
        while p:
            if p.next:  # 处理存在偶数个节点的情况，需要翻转
                q = p.next.next     # 用于记录下次p指针的位置
                r.next = p.next     # 先添加p节点的下一个节点  翻转
                r.next.next = p     # 再添加p节点            翻转
                r = r.next.next     # 更新新链表指针
                p = q
            else:       # 剩余一个节点的情况，直接添加即可
                q = p.next
                r.next = p
                p = q
                r = r.next
        r.next = p  # 将最后的none添加到新链表中
        return result.next</code></pre></div>
