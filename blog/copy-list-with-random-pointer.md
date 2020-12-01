Leetcode 138. 复制带随机指针的链表
<p>给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。</p>


<p>要求返回这个链表的&nbsp;<strong><a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank">深拷贝</a></strong>。&nbsp;</p>



<p>我们用一个由&nbsp;<code>n</code>&nbsp;个节点组成的链表来表示输入/输出中的链表。每个节点用一个&nbsp;<code>[val, random_index]</code>&nbsp;表示：</p>



<ul>

	<li><code>val</code>：一个表示&nbsp;<code>Node.val</code>&nbsp;的整数。</li>

	<li><code>random_index</code>：随机指针指向的节点索引（范围从&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n-1</code>）；如果不指向任何节点，则为&nbsp;&nbsp;<code>null</code>&nbsp;。</li>

</ul>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png" style="height: 138px; width: 680px;"></p>



<pre><strong>输入：</strong>head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

<strong>输出：</strong>[[7,null],[13,0],[11,4],[10,2],[1,0]]

</pre>



<p><strong>示例 2：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png" style="height: 111px; width: 680px;"></p>



<pre><strong>输入：</strong>head = [[1,1],[2,1]]

<strong>输出：</strong>[[1,1],[2,1]]

</pre>



<p><strong>示例 3：</strong></p>



<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png" style="height: 119px; width: 680px;"></strong></p>



<pre><strong>输入：</strong>head = [[3,null],[3,0],[3,null]]

<strong>输出：</strong>[[3,null],[3,0],[3,null]]

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>head = []

<strong>输出：</strong>[]

<strong>解释：</strong>给定的链表为空（空指针），因此返回 null。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>-10000 &lt;= Node.val &lt;= 10000</code></li>

	<li><code>Node.random</code>&nbsp;为空（null）或指向链表中的节点。</li>

	<li>节点数目不超过 1000 。</li>

</ul>





 **难度**: Medium



 **标签**: 哈希表、 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了95.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.26% 的用户

解题思路：
    回溯
    使用head记录已经访问过的节点，和新创建的对应节点
    实现详情见代码注释
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        def backtrack(head, visited):
            if head == None:    # None时，返回None
                return head

            if head in visited: # 如果head访问过了，返回对应的创建的新节点
                return visited[head]

            else:
                node = Node(head.val)   # 没有访问过，创新新节点
                visited[head] = node    # 将新创建的节点，与head绑定，记录到以访问
                node.next = backtrack(head.next, visited)   # 访问head节点的next
                node.random = backtrack(head.random, visited)   # 访问head节点的random
                return node

        node = backtrack(head, {})
        return node
</code></pre></div>
