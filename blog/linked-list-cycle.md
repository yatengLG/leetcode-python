Leetcode 141. 环形链表
<p>给定一个链表，判断链表中是否有环。</p>


<p>如果链表中有某个节点，可以通过连续跟踪 <code>next</code> 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 <code>pos</code> 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 <code>pos</code> 是 <code>-1</code>，则在该链表中没有环。<strong>注意：<code>pos</code> 不作为参数进行传递</strong>，仅仅是为了标识链表的实际情况。</p>



<p>如果链表中存在环，则返回 <code>true</code> 。 否则，返回 <code>false</code> 。</p>



<p>&nbsp;</p>



<p><strong>进阶：</strong></p>



<p>你能用 <em>O(1)</em>（即，常量）内存解决此问题吗？</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" style="height: 97px; width: 300px;"></p>



<pre><strong>输入：</strong>head = [3,2,0,-4], pos = 1

<strong>输出：</strong>true

<strong>解释：</strong>链表中有一个环，其尾部连接到第二个节点。

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 74px; width: 141px;"></p>



<pre><strong>输入：</strong>head = [1,2], pos = 0

<strong>输出：</strong>true

<strong>解释：</strong>链表中有一个环，其尾部连接到第一个节点。

</pre>



<p><strong>示例 3：</strong></p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 45px; width: 45px;"></p>



<pre><strong>输入：</strong>head = [1], pos = -1

<strong>输出：</strong>false

<strong>解释：</strong>链表中没有环。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>链表中节点的数目范围是 <code>[0, 10<sup>4</sup>]</code></li>

	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>

	<li><code>pos</code> 为 <code>-1</code> 或者链表中的一个 <strong>有效索引</strong> 。</li>

</ul>





 **难度**: Easy



 **标签**: 链表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了96.73% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了23.93% 的用户

解题思路：
    快慢指针
    若存在环，快指针会先入环，慢指针后如环。在环中，快慢指针相遇，返回True
    若不存在环，快指针先到达链表末尾
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l, f = ListNode(0, next=head), head # 慢指针，快指针
        while l != f:   # 快慢指针不同，循环
            if f and f.next:
                l = l.next  # 慢指针走一步
                f = f.next.next # 快指针走两步
            else:
                return False    # 若达到链表末尾，则无环
        return True</code></pre></div>
