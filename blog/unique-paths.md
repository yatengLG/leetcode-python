Leetcode 62. 不同路径
<p>一个机器人位于一个 <em>m x n </em>网格的左上角 （起始点在下图中标记为&ldquo;Start&rdquo; ）。</p>


<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为&ldquo;Finish&rdquo;）。</p>



<p>问总共有多少条不同的路径？</p>



<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png"></p>



<p><small>例如，上图是一个7 x 3 的网格。有多少可能的路径？</small></p>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> m = 3, n = 2

<strong>输出:</strong> 3

<strong>解释:</strong>

从左上角开始，总共有 3 条路径可以到达右下角。

1. 向右 -&gt; 向右 -&gt; 向下

2. 向右 -&gt; 向下 -&gt; 向右

3. 向下 -&gt; 向右 -&gt; 向右

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> m = 7, n = 3

<strong>输出:</strong> 28</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= m, n &lt;= 100</code></li>

	<li>题目数据保证答案小于等于 <code>2 * 10 ^ 9</code></li>

</ul>





 **难度**: Medium



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了74.47% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了7.95% 的用户

解题思路：
    只能向右或向下前进。
    则当前格的路径数等于左侧格的路径数+上侧格的路径数
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    例子：
        1   1   1   1   1   1
        1   2   3   4   5   6
        1   3   6   10  15  21
        1   4   10  20  35  56
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)] for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

</code></pre></div>
