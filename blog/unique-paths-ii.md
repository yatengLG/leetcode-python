Leetcode 63. 不同路径 II
<p>一个机器人位于一个 <em>m x n </em>网格的左上角 （起始点在下图中标记为&ldquo;Start&rdquo; ）。</p>


<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为&ldquo;Finish&rdquo;）。</p>



<p>现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？</p>



<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png" style="height: 183px; width: 400px;"></p>



<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。</p>



<p><strong>说明：</strong><em>m</em>&nbsp;和 <em>n </em>的值均不超过 100。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:

</strong>[

&nbsp; [0,0,0],

&nbsp; [0,1,0],

&nbsp; [0,0,0]

]

<strong>输出:</strong> 2

<strong>解释:</strong>

3x3 网格的正中间有一个障碍物。

从左上角到右下角一共有 <code>2</code> 条不同的路径：

1. 向右 -&gt; 向右 -&gt; 向下 -&gt; 向下

2. 向下 -&gt; 向下 -&gt; 向右 -&gt; 向右

</pre>





 **难度**: Medium



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.17% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了75.98% 的用户

解题思路：
    动态规划
    由于网格中加入了障碍
    障碍右侧的网格路径数，只依赖于网格上侧
    障碍下侧的网格路径数，只依赖于网格左侧
    为统一思路，将存在障碍的网格路径数置为0 即可
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[1 for _ in range(m)] for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0

        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
</code></pre></div>
