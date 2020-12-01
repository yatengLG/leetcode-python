Leetcode 109. 有序链表转换二叉搜索树
<p>给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。</p>


<p>本题中，一个高度平衡二叉树是指一个二叉树<em>每个节点&nbsp;</em>的左右两个子树的高度差的绝对值不超过 1。</p>



<p><strong>示例:</strong></p>



<pre>给定的有序链表： [-10, -3, 0, 5, 9],



一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：



      0

     / \

   -3   9

   /   /

 -10  5

</pre>





 **难度**: Medium



 **标签**: 深度优先搜索、 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：152 ms, 在所有 Python3 提交中击败了5.29% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了59.61% 的用户

解题思路：
    双指针找中心，然后生成树
    具体实现见代码注释
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:    # 如果当前链表为空，返回空
            return None
        if head.next == None:   # 如果当前链表为单个元素，返回结点
            return TreeNode(head.val)

        pre = ListNode(0)
        pre.next = head
        fast, slow = head, pre  # 快慢指针
        while True:
            fast = fast.next.next   # 循环完成后，slow指向中点前的一个元素
            slow = slow.next
            if fast == None or fast.next == None:
                break

        node = slow.next    # 中间元素
        right_link = slow.next.next # 右半部分链表
        slow.next = None    # 截断链表
        left_link = pre.next    # 左半部分链表
        node = TreeNode(node.val)   # 当前树根结点
        node.left = self.sortedListToBST(left_link) # 递归寻找左子树中间值
        node.right = self.sortedListToBST(right_link)   # 寻找右子树中间值

        return node

"""
执行用时：148 ms, 在所有 Python3 提交中击败了5.29% 的用户
内存消耗：19.9 MB, 在所有 Python3 提交中击败了22.42% 的用户

解题思路：
    先将链表转换为python列表再进行操作。
    性能与上例是相同的，但是对python来说更好理解一些
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        link_list = []
        while head:
            link_list.append(head.val)
            head = head.next

        def f(link_list):
            n = len(link_list)
            if n == 0:
                return None
            if n == 1:
                return TreeNode(link_list[0])
            m = n // 2
            node = TreeNode(link_list[m])
            node.left = f(link_list[:m])
            node.right = f(link_list[m + 1:])
            return node

        return f(link_list)</code></pre></div>
