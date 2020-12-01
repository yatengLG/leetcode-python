Leetcode 725. 分隔链表
<p>给定一个头结点为 <code>root</code> 的链表, 编写一个函数以将链表分隔为 <code>k</code> 个连续的部分。</p>


<p>每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。</p>



<p>这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。</p>



<p>返回一个符合上述规则的链表的列表。</p>



<p>举例： 1-&gt;2-&gt;3-&gt;4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]</p>



<p><strong>示例 1：</strong></p>



<pre>

<strong>输入:</strong> 

root = [1, 2, 3], k = 5

<strong>输出:</strong> [[1],[2],[3],[],[]]

<strong>解释:</strong>

输入输出各部分都应该是链表，而不是数组。

例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且 root.next.next.next = null。

第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。

最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。

</pre>



<p><strong>示例 2：</strong></p>



<pre>

<strong>输入:</strong> 

root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3

<strong>输出:</strong> [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

<strong>解释:</strong>

输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。

</pre>



<p>&nbsp;</p>



<p><strong>提示:</strong></p>



<ul>

	<li><code>root</code> 的长度范围：&nbsp;<code>[0, 1000]</code>.</li>

	<li>输入的每个节点的大小范围：<code>[0, 999]</code>.</li>

	<li><code>k</code>&nbsp;的取值范围：&nbsp;<code>[1, 50]</code>.</li>

</ul>



<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 链表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了99.63% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了12.97% 的用户

解题思路：
    先将链表拆分为单个节点，并统计链长度
    根据链表长度以及k，计算，每段的节点个数以及多余的节点数
    按照计算结果连接链表
    具体实现见代码注释
"""
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        record = [] # 列表保存拆分成单个的节点
        r = root
        num = 0     # 统计链表长度
        while r:    # 拆分链表节点
            r_next = r.next
            r.next = None
            record.append(r)
            r = r_next
            num += 1

        result = [] # 最终结果
        remainder = num % k # 计算分段后的多余节点数
        n = num // k    # 每段的个数
        if n < 1:
            return record + [None] * (k - num)

        start_index = 0 # 起始位置
        for i in range(k):
            if remainder > 0:   # 如果还有多余的节点，则前几段每段多一个节点
                nodes = record[start_index:start_index + n + 1]
                start_index += n + 1
                remainder -= 1  # 多余节点数-1
            else:
                nodes = record[start_index:start_index + n]
                start_index += n

            nodes += [None]
            for j, node in enumerate(nodes):    # 重组每段链表
                if node:
                    node.next = nodes[j + 1]
            result.append(nodes[0]) # 将重组后的每段链表添加到最终结果中
        return result
</code></pre></div>
