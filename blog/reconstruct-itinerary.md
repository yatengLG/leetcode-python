Leetcode 332. 重新安排行程
<p>给定一个机票的字符串二维数组 <code>[from, to]</code>，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。</p>


<p><strong>说明:</strong></p>



<ol>

	<li>如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 [&quot;JFK&quot;, &quot;LGA&quot;] 与 [&quot;JFK&quot;, &quot;LGB&quot;] 相比就更小，排序更靠前</li>

	<li>所有的机场都用三个大写字母表示（机场代码）。</li>

	<li>假定所有机票至少存在一种合理的行程。</li>

</ol>



<p><strong>示例 1:</strong></p>



<pre><code><strong>输入: </strong></code><code>[[&quot;MUC&quot;, &quot;LHR&quot;], [&quot;JFK&quot;, &quot;MUC&quot;], [&quot;SFO&quot;, &quot;SJC&quot;], [&quot;LHR&quot;, &quot;SFO&quot;]]</code>

<strong>输出: </strong><code>[&quot;JFK&quot;, &quot;MUC&quot;, &quot;LHR&quot;, &quot;SFO&quot;, &quot;SJC&quot;]</code>

</pre>



<p><strong>示例 2:</strong></p>



<pre><code><strong>输入: </strong></code><code>[[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]</code>

<strong>输出: </strong><code>[&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>

<strong>解释: </strong>另一种有效的行程是&nbsp;<code>[&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>。但是它自然排序更大更靠后。</pre>





 **难度**: Medium



 **标签**: 深度优先搜索、 图、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了95.23% 的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了36.92% 的用户

解题思路：
    回溯
    具体见代码注释
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict # 由于存在有的节点没有指向的情况，需要给终点一个默认值
        records = defaultdict(list) # 字典，用于存储 当前节点可以通向的节点 {from :[to_1, to_2, to_3, ...]}
        for ticket in tickets:
            if ticket[0] not in records:
                records[ticket[0]] = [ticket[1]]
            else:
                records[ticket[0]].append(ticket[1])
                records[ticket[0]].sort()   # 为了方便处理，对通向的节点进行一个排序

        result = ['JFK']    # result保存最终的路径，其实点为'jfk'
        def find(start):    # 回溯
            if len(result) == len(tickets)+1:   # 如果路径都走过了，则返回true  。result包含路径与起始点.
                return True
            tos = records[start]    # 当前节点 可通向的节点
            for to in tos:
                to = tos.pop(0)     # 取出一个节点，加入最终路径result中
                result.append(to)
                if find(to):        # 以当前节点继续走，如果当前节点符合最终路径要求，return
                    return True
                result.pop()        # 当前节点继续走，不符合最终路径要求，回溯，将当前节点从最终路径中删除
                records[start].append(to)   # 将当前节点存回 字典中
            return False

        find(start='JFK')
        return result
</code></pre></div>
