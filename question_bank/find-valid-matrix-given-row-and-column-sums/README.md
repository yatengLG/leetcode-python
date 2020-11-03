<h2>1605. 给定行和列的和求可行矩阵</h2><p>给你两个非负整数数组&nbsp;<code>rowSum</code> 和&nbsp;<code>colSum</code>&nbsp;，其中&nbsp;<code>rowSum[i]</code>&nbsp;是二维矩阵中第 <code>i</code>&nbsp;行元素的和， <code>colSum[j]</code>&nbsp;是第 <code>j</code>&nbsp;列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。</p>

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


------

<h2>1605. Find Valid Matrix Given Row and Column Sums</h2><p>You are given two arrays <code>rowSum</code> and <code>colSum</code> of non-negative integers where <code>rowSum[i]</code> is the sum of the elements in the <code>i<sup>th</sup></code> row and <code>colSum[j]</code> is the sum of the elements of the <code>j<sup>th</sup></code> column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.</p>

<p>Find any matrix of <strong>non-negative</strong> integers of size <code>rowSum.length x colSum.length</code> that satisfies the <code>rowSum</code> and <code>colSum</code> requirements.</p>

<p>Return <em>a 2D array representing <strong>any</strong> matrix that fulfills the requirements</em>. It&#39;s guaranteed that <strong>at least one </strong>matrix that fulfills the requirements exists.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> rowSum = [3,8], colSum = [4,7]
<strong>Output:</strong> [[3,0],
         [1,7]]
<strong>Explanation:</strong>
0th row: 3 + 0 = 0 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> rowSum = [5,7,10], colSum = [8,6,8]
<strong>Output:</strong> [[0,5,0],
         [6,1,0],
         [2,0,8]]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> rowSum = [14,9], colSum = [6,9,8]
<strong>Output:</strong> [[0,9,5],
         [6,0,3]]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> rowSum = [1,0], colSum = [1]
<strong>Output:</strong> [[1],
         [0]]
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> rowSum = [0], colSum = [0]
<strong>Output:</strong> [[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= rowSum.length, colSum.length &lt;= 500</code></li>
	<li><code>0 &lt;= rowSum[i], colSum[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>sum(rows) == sum(columns)</code></li>
</ul>

 **difficulty**: Medium

 **topic**: Greedy, 

