Leetcode 61. 旋转链表
<p>给定一个链表，旋转链表，将链表每个节点向右移动&nbsp;<em>k&nbsp;</em>个位置，其中&nbsp;<em>k&nbsp;</em>是非负数。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> 1-&gt;2-&gt;3-&gt;4-&gt;5-&gt;NULL, k = 2

<strong>输出:</strong> 4-&gt;5-&gt;1-&gt;2-&gt;3-&gt;NULL

<strong>解释:</strong>

向右旋转 1 步: 5-&gt;1-&gt;2-&gt;3-&gt;4-&gt;NULL

向右旋转 2 步: 4-&gt;5-&gt;1-&gt;2-&gt;3-&gt;NULL

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> 0-&gt;1-&gt;2-&gt;NULL, k = 4

<strong>输出:</strong> <code>2-&gt;0-&gt;1-&gt;NULL</code>

<strong>解释:</strong>

向右旋转 1 步: 2-&gt;0-&gt;1-&gt;NULL

向右旋转 2 步: 1-&gt;2-&gt;0-&gt;NULL

向右旋转 3 步:&nbsp;<code>0-&gt;1-&gt;2-&gt;NULL</code>

向右旋转 4 步:&nbsp;<code>2-&gt;0-&gt;1-&gt;NULL</code></pre>





 **难度**: Medium



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.33% 的用户
内存消耗：13.1 MB, 在所有 Python3 提交中击败了98.58% 的用户

解题思路：
    双指针，
    将p指针移动k步，然后移动q指针，找到移动后的链表首位。此时，q的next指向移动后的链表首位，p指针指向原链表末尾
    需注意大于链表长度的移动
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:    # 链表为空，直接返回
            return head
        if k == 0:  # 移动0步，直接返回
            return head
        p, q = head, head   # 双指针
        repeat = False  # 是否超出了链表长度
        for i in range(k):  # 循环k步
            if p.next:  # 移动p指针
                p = p.next
            else:   # 超出链表长度，重新计算移动的步数
                k = k % (i+1)
                repeat = True
                break
        if repeat:  # 超出链表长度，重新计算
            return self.rotateRight(head, k)

        while p.next:   # 移动p, q指针，直到p指针指向原链表末尾。此时q指针next指向移动后的链表首位
            p = p.next
            q = q.next
        result = q.next # 组合新链表
        p.next = head
        q.next = None
        return result</code></pre></div>
