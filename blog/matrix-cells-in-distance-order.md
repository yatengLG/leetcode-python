Leetcode 1030. 距离顺序排列矩阵单元格
<p>给出 <code>R</code> 行 <code>C</code> 列的矩阵，其中的单元格的整数坐标为 <code>(r, c)</code>，满足 <code>0 &lt;= r &lt; R</code> 且 <code>0 &lt;= c &lt; C</code>。</p>


<p>另外，我们在该矩阵中给出了一个坐标为&nbsp;<code>(r0, c0)</code> 的单元格。</p>



<p>返回矩阵中的所有单元格的坐标，并按到 <code>(r0, c0)</code> 的距离从最小到最大的顺序排，其中，两单元格<code>(r1, c1)</code> 和 <code>(r2, c2)</code> 之间的距离是曼哈顿距离，<code>|r1 - r2| + |c1 - c2|</code>。（你可以按任何满足此条件的顺序返回答案。）</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>R = 1, C = 2, r0 = 0, c0 = 0

<strong>输出：</strong>[[0,0],[0,1]]

<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>R = 2, C = 2, r0 = 0, c0 = 1

<strong>输出：</strong>[[0,1],[0,0],[1,1],[1,0]]

<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]

[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>R = 2, C = 3, r0 = 1, c0 = 2

<strong>输出：</strong>[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]

<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]

其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= R &lt;= 100</code></li>

	<li><code>1 &lt;= C &lt;= 100</code></li>

	<li><code>0 &lt;= r0 &lt; R</code></li>

	<li><code>0 &lt;= c0 &lt; C</code></li>

</ol>





 **难度**: Easy



 **标签**: 排序、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG


"""
执行用时：196 ms
内存消耗：15.6 MB
解题思路：
    将所有的点存在一个列表里。
    对列表按距离进行排序。
    最简洁，但也最慢。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        lists = [[r, c] for r in range(R) for c in range(C)]
        lists = sorted(lists, key=lambda p: abs(p[0]-r0)+abs(p[1]-c0))
        return lists


"""
执行用时：180 ms, 在所有 Python3 提交中击败了72.17% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了100.00% 的用户
解题思路：
    循环计算各点与原点距离，存入一个列表中，将同距离点都存在一个列表中，列表第一个元素中存储距离为1的点，第二个元素中存储距离为2的点。
    遍历列表，获取点。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        dists = [[] for _ in range(R+C)]
        for r in range(abs(R)):
            for c in range(abs(C)):
                dists[abs(r-r0)+abs(c-c0)].append([r, c])

        result = []
        for dist in dists:
            if dist !=[]:
                result.extend(dist)
        return result


"""
执行用时：172 ms
内存消耗：15.3 MB
解题思路：
    思路与2相同，但将列表换成字段。
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        dists = {}
        for r in range(abs(R)):
            for c in range(abs(C)):
                dist = abs(r-r0)+abs(c-c0)
                if dist not in dists.keys():
                    dists[dist] = []
                dists[dist].append([r, c])
        result = []
        dists_keys = sorted(dists.keys())
        for dist in dists_keys:
            result.extend(dists[dist])
        return result
</code></pre></div>
