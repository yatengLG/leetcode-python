Leetcode 463. 岛屿的周长
<p>给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地&nbsp;0 表示水域。</p>


<p>网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。</p>



<p>岛屿中没有&ldquo;湖&rdquo;（&ldquo;湖&rdquo; 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。</p>



<p>&nbsp;</p>



<p><strong>示例 :</strong></p>



<pre><strong>输入:</strong>

[[0,1,0,0],

 [1,1,1,0],

 [0,1,0,0],

 [1,1,0,0]]



<strong>输出:</strong> 16



<strong>解释:</strong> 它的周长是下面图片中的 16 个黄色的边：



<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/island.png">

</pre>





 **难度**: Easy



 **标签**: 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：152 ms, 在所有 Python3 提交中击败了68.28% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了58.86% 的用户

解题思路：
    每存在一个相邻岛屿，则边各少一条。
    具体实现见代码注释
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num = 0 # 记录岛屿数
        neighbor = 0    # 记录相邻岛屿数
        m, n = len(grid), len(grid[0])  #
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # 找到岛屿
                    num += 1    # 岛屿数+1
                    if 0 <= i-1 and grid[i-1][j] == 1:  # 查看岛屿四周，找相邻岛屿
                        neighbor += 1   # 存在相邻岛屿，相邻岛屿数+1
                    if i+1 < m and grid[i+1][j] == 1:
                        neighbor += 1
                    if 0 <= j-1 and grid[i][j-1] == 1:
                        neighbor += 1
                    if j+1 < n and grid[i][j+1] == 1:
                        neighbor += 1
        return num*4-neighbor</code></pre></div>
