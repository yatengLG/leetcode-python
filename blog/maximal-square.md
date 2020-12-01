Leetcode 221. 最大正方形
<p>在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入: 

</strong>

1 0 1 0 0

1 0 <strong>1 1</strong> 1

1 1 <strong>1 1 </strong>1

1 0 0 1 0



<strong>输出: </strong>4</pre>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：84 ms, 在所有 Python3 提交中击败了93.21% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了27.86% 的用户

解题思想：

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_ = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_ = max(dp[i][0], max_)

        for j in range(1, n):
            dp[0][j] = int(matrix[0][j])
            max_ = max(dp[0][j], max_)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0

                max_ = max(dp[i][j], max_)
        return max_**2


"""
执行用时：120 ms, 在所有 Python3 提交中击败了30.10% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了61.68% 的用户

解题思路：
    整理代码后，效率变低，但是逻辑上更顺畅
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_ = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i+1-1][j+1-1], dp[i+1][j+1-1], dp[i+1-1][j+1]) + 1
                else:
                    dp[i+1][j+1] = 0

                max_ = max(dp[i+1][j+1], max_)
        return max_**2</code></pre></div>
