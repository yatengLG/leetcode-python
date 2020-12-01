Leetcode 1605. 给定行和列的和求可行矩阵
<p>给你两个非负整数数组&nbsp;<code>rowSum</code> 和&nbsp;<code>colSum</code>&nbsp;，其中&nbsp;<code>rowSum[i]</code>&nbsp;是二维矩阵中第 <code>i</code>&nbsp;行元素的和， <code>colSum[j]</code>&nbsp;是第 <code>j</code>&nbsp;列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。</p>


<p>请找到大小为&nbsp;<code>rowSum.length x colSum.length</code>&nbsp;的任意 <strong>非负整数</strong>&nbsp;矩阵，且该矩阵满足&nbsp;<code>rowSum</code> 和&nbsp;<code>colSum</code>&nbsp;的要求。</p>



<p>请你返回任意一个满足题目要求的二维矩阵，题目保证存在 <strong>至少一个</strong>&nbsp;可行矩阵。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>rowSum = [3,8], colSum = [4,7]

<strong>输出：</strong>[[3,0],

      [1,7]]

<strong>解释：</strong>

第 0 行：3 + 0 = 0 == rowSum[0]

第 1 行：1 + 7 = 8 == rowSum[1]

第 0 列：3 + 1 = 4 == colSum[0]

第 1 列：0 + 7 = 7 == colSum[1]

行和列的和都满足题目要求，且所有矩阵元素都是非负的。

另一个可行的矩阵为：[[1,2],

                  [3,5]]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>rowSum = [5,7,10], colSum = [8,6,8]

<strong>输出：</strong>[[0,5,0],

      [6,1,0],

      [2,0,8]]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>rowSum = [14,9], colSum = [6,9,8]

<strong>输出：</strong>[[0,9,5],

      [6,0,3]]

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>rowSum = [1,0], colSum = [1]

<strong>输出：</strong>[[1],

      [0]]

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入：</strong>rowSum = [0], colSum = [0]

<strong>输出：</strong>[[0]]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= rowSum.length, colSum.length &lt;= 500</code></li>

	<li><code>0 &lt;= rowSum[i], colSum[i] &lt;= 10<sup>8</sup></code></li>

	<li><code>sum(rows) == sum(columns)</code></li>

</ul>





 **难度**: Medium



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了90.00% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了13.51% 的用户

解题思路：
    贪心算法
    在每个空缺处，填可以填的最大值
    在每个空缺处填入行列和中的最小值，则填完后，必然会有行列和中的某一值为0，可以直接跳过该行/列，提高效率
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        result = [[0 for _ in range(c)] for _ in range(r)]
        i, j = 0, 0
        while i < r and j < c:
            val = min(rowSum[i], colSum[j]) # 取当前空位对应行列值的最小值，填入该空位
            result[i][j] = val

            rowSum[i] -= val    # 因为填的是当前行列中最小的那个，则每次填完，则必有行列之一的和为0，直接跳过当前行列即可
            if rowSum[i] == 0:
                i += 1

            colSum[j] -= val
            if colSum[j] == 0:
                j += 1

        return result


"""
执行用时：324 ms, 在所有 Python3 提交中击败了74.59% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了17.57% 的用户

解题思路：
    贪心算法
    在每个空缺处，填可以填的最大值
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        result = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                val = min(rowSum[i], colSum[j]) # 取当前空位对应行列值的最小值，填入该空位
                result[i][j] = val
                rowSum[i] -= val    # 更新当前行列的和的值
                colSum[j] -= val
        return result</code></pre></div>
