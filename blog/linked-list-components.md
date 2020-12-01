Leetcode 817. 链表组件
<p>给定链表头结点&nbsp;<code>head</code>，该链表上的每个结点都有一个 <strong>唯一的整型值</strong> 。</p>


<p>同时给定列表&nbsp;<code>G</code>，该列表是上述链表中整型值的一个子集。</p>



<p>返回列表&nbsp;<code>G</code>&nbsp;中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表&nbsp;<code>G</code>&nbsp;中）构成的集合。</p>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1：</strong></p>



<pre><strong>输入:</strong> 

head: 0-&gt;1-&gt;2-&gt;3

G = [0, 1, 3]

<strong>输出:</strong> 2

<strong>解释:</strong> 

链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入:</strong> 

head: 0-&gt;1-&gt;2-&gt;3-&gt;4

G = [0, 3, 1, 4]

<strong>输出:</strong> 2

<strong>解释:</strong> 

链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>如果&nbsp;<code>N</code>&nbsp;是给定链表&nbsp;<code>head</code>&nbsp;的长度，<code>1 &lt;= N &lt;= 10000</code>。</li>

	<li>链表中每个结点的值所在范围为&nbsp;<code>[0, N - 1]</code>。</li>

	<li><code>1 &lt;= G.length &lt;= 10000</code></li>

	<li><code>G</code> 是链表中所有结点的值的一个子集.</li>

</ul>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG


"""
执行用时：100 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：18 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    遍历链表，查看是否存在与G中，如存在，就算一个组件，直到下次出现断开的情况
    添加了G = set(G)
"""
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        num = 0
        start = False   # 用于记录是否连续
        while head:
            if head.val in G:
                G.remove(head.val)
                if not start:   # 与前面不连续，则为一个新租件
                    start = True
                    num += 1
            else:   # 当前值不在G中，断开
                start = False
            head = head.next
        return num
</code></pre></div>
