Leetcode 685. 冗余连接 II
<p>在本问题中，有根树指满足以下条件的<strong>有向</strong>图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。</p>


<p>输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。</p>



<p>结果图是一个以<code>边</code>组成的二维数组。 每一个<code>边</code> 的元素是一对 <code>[u, v]</code>，用以表示<strong>有向</strong>图中连接顶点 <code>u</code> 和顶点 <code>v</code> 的边，其中 <code>u</code> 是 <code>v</code> 的一个父节点。</p>



<p>返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> [[1,2], [1,3], [2,3]]

<strong>输出:</strong> [2,3]

<strong>解释:</strong> 给定的有向图如下:

  1

 / \

v   v

2--&gt;3

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [[1,2], [2,3], [3,4], [4,1], [1,5]]

<strong>输出:</strong> [4,1]

<strong>解释:</strong> 给定的有向图如下:

5 &lt;- 1 -&gt; 2

     ^    |

     |    v

     4 &lt;- 3

</pre>



<p><strong>注意:</strong></p>



<ul>

	<li>二维数组大小的在3到1000范围内。</li>

	<li>二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。</li>

</ul>





 **难度**: Hard



 **标签**: 树、 深度优先搜索、 并查集、 图、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：116 ms, 在所有 Python3 提交中击败了8.59% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了5.71% 的用户

解题思路：
    1.  [1,2], [2,3], [3,1]     # 成环
    1.1     [1,2], [2,3], [3,1], [4,1]  # 成环，且有入度大于1的点(仅可有一个)
    1.2     [1,2], [2,3], [3,1], [1,4]  # 成环，且有分支
    2.  [1,2], [2,3], [1,3]     # 不成环， 入度大于1
    1.1     [1,2], [2,3], [1,3], [4,1]  # 不成环，入度大于1，入分支
    1.2     [1,2], [2,3], [1,3], [1,4]  # 不成环，入度大于1，出分支

    经过整合，可整合为两种情况:
        1. 存在入度大于1 的点，多余的边必定是入度大于1的边，
            1.1 若成环，则删除成环的那条入度大于1的边
            1.2 若不成环，删除最后添加的那条入度大于1的边
        2. 不存在入度大于1 的点，则必然有环
            删除最后添加的环中的边

"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        def is_cycle(start, used, to_dict): # 起始点，当前通过的路径，路径字典
            # print(start, used, to_dict)
            if start not in used:   # 如果当前起始点没有经过，则不成环
                nexts = to_dict[start]  # 当前起始点可以去的节点
                if nexts != []:
                    next = nexts[-1]    # 取最后一个可以去的节点
                    to_dict[start].pop(-1)  # 删除取过的路径
                    if is_cycle(next, used+[start], to_dict):   # 找下一个路径
                        return True
                else:
                    return
            else:
                for i ,e in enumerate(used):    # 当前路径成环，但不一定只有环，这里将对于的节点删掉
                    if e == start:
                        self.circle = used[i:] + [start]
                        break
                return True

        self.circle = []    # 用于记录环
        to_dict = defaultdict(list) # 路径字典
        to_list = []
        to_ = None

        for edge in edges:
            to_dict[edge[0]].append(edge[1])
            if edge[1] not in to_list:
                to_list.append(edge[1])
            else:
                to_ = edge[1]   # 入度等于2的点


        if to_ is None: # 没有入度大于1的点, 必有环，找环
            for edge in edges[::-1]:    # 因为需要删除最后出现在数组中的答案，这里反序检查。
                start = edge[0]
                if is_cycle(start, [], to_dict):  # 找环
                    self.circle = [[self.circle[i], self.circle[i+1]] for i in range(len(self.circle)-1)]
                    return self.circle[0]

        else:   # 存在入度大于1的点，在本题中只可能存在一个,且入度为2
            tos_ = []   # 保存入度为2 的两条路径
            for edge in edges[::-1]:    # 找环,此时只需找入度为2的点是否存在环即可
                if edge[-1] == to_:
                    tos_.append(edge)
                    if self.circle == []: # 没找到环时，继续找，找到就不需要了
                        if is_cycle(edge[0], [], to_dict):
                            self.circle = [[self.circle[i], self.circle[i + 1]] for i in range(len(self.circle)-1)]

            for t in tos_[::-1]:
                if t in self.circle:
                    return t
            return tos_[0]

</code></pre></div>
