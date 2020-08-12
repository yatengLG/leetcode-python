# -*- coding: utf-8 -*-
# @Author  : LG

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
执行用时：44 ms, 在所有 Python3 提交中击败了93.79% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了94.12% 的用户

解题思路：
    这个题想半天没想出来，然后看了别人解题才想明白这题要干啥
    题目的意思是需要删除这个节点，直接把这个节点的值与next更新为下一个即可

"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next