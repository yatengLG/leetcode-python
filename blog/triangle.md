Leetcode 120. 三角形最小路径和
<p>给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。</p>


<p><strong>相邻的结点 </strong>在这里指的是 <code>下标</code> 与 <code>上一层结点下标</code> 相同或者等于 <code>上一层结点下标 + 1</code> 的两个结点。</p>



<p>&nbsp;</p>



<p>例如，给定三角形：</p>



<pre>[

     [<strong>2</strong>],

    [<strong>3</strong>,4],

   [6,<strong>5</strong>,7],

  [4,<strong>1</strong>,8,3]

]

</pre>



<p>自顶向下的最小路径和为&nbsp;<code>11</code>（即，<strong>2&nbsp;</strong>+&nbsp;<strong>3</strong>&nbsp;+&nbsp;<strong>5&nbsp;</strong>+&nbsp;<strong>1</strong>&nbsp;= 11）。</p>



<p>&nbsp;</p>



<p><strong>说明：</strong></p>



<p>如果你可以只使用 <em>O</em>(<em>n</em>)&nbsp;的额外空间（<em>n</em> 为三角形的总行数）来解决这个问题，那么你的算法会很加分。</p>





 **难度**: Medium



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了72.15% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了62.55% 的用户

解题思路：
    自顶向下叠加
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            m = len(triangle[i])
            for j in range(m):
                if j-1 < 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j+1 > m-1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        return min(triangle[-1])


"""
执行用时：44 ms, 在所有 Python3 提交中击败了88.51% 的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了30.46% 的用户

解题思路：
    自底向上，省去了边界判断以及最后的找最小值
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n-1, 0, -1):
            for j in range(i):  # 第n行有n-1个元素，
                triangle[i-1][j] = min(triangle[i][j], triangle[i][j+1]) + triangle[i-1][j] # 上一行的元素等于 上一行元素+ 本行相邻元素的最小值
        return triangle[0][0]</code></pre></div>
