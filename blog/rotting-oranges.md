Leetcode 994. 腐烂的橘子
<p>在给定的网格中，每个单元格可以有以下三个值之一：</p>


<ul>

	<li>值&nbsp;<code>0</code>&nbsp;代表空单元格；</li>

	<li>值&nbsp;<code>1</code>&nbsp;代表新鲜橘子；</li>

	<li>值&nbsp;<code>2</code>&nbsp;代表腐烂的橘子。</li>

</ul>



<p>每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。</p>



<p>返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回&nbsp;<code>-1</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png" style="height: 150px; width: 712px;"></strong></p>



<pre><strong>输入：</strong>[[2,1,1],[1,1,0],[0,1,1]]

<strong>输出：</strong>4

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[[2,1,1],[0,1,1],[1,0,1]]

<strong>输出：</strong>-1

<strong>解释：</strong>左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>[[0,2]]

<strong>输出：</strong>0

<strong>解释：</strong>因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= grid.length &lt;= 10</code></li>

	<li><code>1 &lt;= grid[0].length &lt;= 10</code></li>

	<li><code>grid[i][j]</code> 仅为&nbsp;<code>0</code>、<code>1</code>&nbsp;或&nbsp;<code>2</code></li>

</ol>





 **难度**: Medium



 **标签**: 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了93.91% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了86.67% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        roted = []  # 保存坏橘子的坐标
        empty = []  # 保存空坐标
        fresh = []  # 保存新鲜的橘子的坐标
        h, w = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 上下左右四个移动方向

        # 遍历格子，记录坏橘子，空格子，新鲜橘子的坐标
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 2:
                    roted.append((i, j))
                elif grid[i][j] == 1:
                    fresh.append((i, j))
                elif grid[i][j] == 0:
                    empty.append((i, j))

        if roted == []: # 如果没有坏橘子
            if fresh:   # 如果有新鲜的，则返回-1（因为没有坏橘子，不会感染）
                return -1
            else:   # 否则，没有新鲜橘子，返回0
                return 0

        num = 0 # 用于记录时间
        while roted:
            num += 1
            new_roted = []  # 记录新腐烂的橘子坐标
            for rot in roted:   # 从已经腐烂的橘子坐标开始
                for d in directions:    # 查看四个方向
                    new_i = rot[0] + d[0]
                    new_j = rot[1] + d[1]
                    if (new_i, new_j) in fresh: # 如果当前坐标存在好橘子
                        fresh.remove((new_i, new_j))    # 则从好橘子列表中删除，当前坐标
                        new_roted.append((new_i, new_j))    # 在新腐烂的橘子列表中记录当前坐标

            roted = new_roted[:]    # 更新坏橘子列表，下次从新腐烂的开始
        if fresh:   # 如果感染完后，存在新鲜橘子，则返回-1
            return -1
        else:       # 否则， 返回0
            return num-1
</code></pre></div>
