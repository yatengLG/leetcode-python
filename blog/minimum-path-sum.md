Leetcode 64. 最小路径和
<p>给定一个包含非负整数的 <em>m</em>&nbsp;x&nbsp;<em>n</em>&nbsp;网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>


<p><strong>说明：</strong>每次只能向下或者向右移动一步。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong>

[

&nbsp; [1,3,1],

  [1,5,1],

  [4,2,1]

]

<strong>输出:</strong> 7

<strong>解释:</strong> 因为路径 1&rarr;3&rarr;1&rarr;1&rarr;1 的总和最小。

</pre>





 **难度**: Medium



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了99.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了8.33% 的用户

解题思路：
    计算每个点 上侧与左侧的最小值，作为当前点到左上点的最短距离。
    依次计算，直到遍历完整个路径矩阵
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        for i in range(n):
            if i >0:
                grid[i][0] = grid[i-1][0] + grid[i][0]
            else:
                grid[i][0] = 0 + grid[i][0]

        for j in range(1, m):
            grid[0][j] = grid[0][j-1] + grid[0][j]

        if m > 1:
            for i in range(1, n):
                if n >1:
                    for j in range(1, m):
                        grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[n-1][m-1]


</code></pre></div>
