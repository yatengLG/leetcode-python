Leetcode 304. 二维区域和检索 - 矩阵不可变
<p>给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (<em>row</em>1,&nbsp;<em>col</em>1) ，右下角为 (<em>row</em>2,&nbsp;<em>col</em>2)。</p>


<p><img alt="Range Sum Query 2D" src="https://assets.leetcode-cn.com/aliyun-lc-upload/images/304.png" style="width: 130px;"><br>

<small>上图子矩阵左上角&nbsp;(row1, col1) = <strong>(2, 1)</strong>&nbsp;，右下角(row2, col2) = <strong>(4, 3)，</strong>该子矩形内元素的总和为 8。</small></p>



<p><strong>示例:</strong></p>



<pre>给定 matrix = [

  [3, 0, 1, 4, 2],

  [5, 6, 3, 2, 1],

  [1, 2, 0, 1, 5],

  [4, 1, 0, 1, 7],

  [1, 0, 3, 0, 5]

]



sumRegion(2, 1, 4, 3) -&gt; 8

sumRegion(1, 1, 2, 2) -&gt; 11

sumRegion(1, 2, 2, 4) -&gt; 12

</pre>



<p><strong>说明:</strong></p>



<ol>

	<li>你可以假设矩阵不可变。</li>

	<li>会多次调用&nbsp;<em>sumRegion&nbsp;</em>方法<em>。</em></li>

	<li>你可以假设&nbsp;<em>row</em>1 &le; <em>row</em>2 且&nbsp;<em>col</em>1 &le; <em>col</em>2。</li>

</ol>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：128 ms, 在所有 Python3 提交中击败了92.83% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了29.48% 的用户

解题思路：
    动态规划
    计算 左上角到某一点的 和

    计算两点之间的和时， 等于右下角点到原点的和 - 上侧 - 左侧 + 左上角到原点的和
"""
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix and matrix[0]:
            self.m = len(matrix)
            self.n = len(matrix[0])

            self.dp = [[0 for _ in range(self.n+1)] for _ in range(self.m+1)]

            for i in range(1, self.m+1):
                for j in range(1, self.n+1):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return 0
        # print(self.dp)
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        # print(self.dp[row2][col2], self.dp[row1-1][col1], self.dp[row1][col1-1], self.dp[row1-1][col1-1])
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
</code></pre></div>
