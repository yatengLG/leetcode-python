Leetcode 234. 回文链表
<p>请判断一个链表是否为回文链表。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> 1-&gt;2

<strong>输出:</strong> false</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> 1-&gt;2-&gt;2-&gt;1

<strong>输出:</strong> true

</pre>



<p><strong>进阶：</strong><br>

你能否用&nbsp;O(n) 时间复杂度和 O(1) 空间复杂度解决此题？</p>





 **难度**: Easy



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
执行用时：76 ms, 在所有 Python3 提交中击败了90.65% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了57.77% 的用户

解题思路：
    快慢指针，使用慢指针找链表中心，将后半部分翻转
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head

        while fast and fast.next:   # 快慢指针，快指针是慢指针的2倍速,当快指针到达链表末尾时，慢指针刚好到一半
            fast = fast.next.next
            slow = slow.next

        reverse = None
        while slow: # 慢指针翻转链表后半部分
            i = slow
            slow = slow.next
            i.next = reverse
            reverse = i

        while head and reverse: # 进行比较
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next

        return True</code></pre></div>
