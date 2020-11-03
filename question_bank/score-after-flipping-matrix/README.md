<h2>861. 翻转矩阵后的得分</h2><p>有一个二维矩阵&nbsp;<code>A</code> 其中每个元素的值为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;。</p>

<p>移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 <code>0</code> 都更改为 <code>1</code>，将所有 <code>1</code> 都更改为 <code>0</code>。</p>

<p>在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。</p>

<p>返回尽可能高的分数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
<strong>输出：</strong>39
<strong>解释：
</strong>转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20</code></li>
	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
	<li><code>A[i][j]</code>&nbsp;是&nbsp;<code>0</code> 或&nbsp;<code>1</code></li>
</ol>


 **难度**: Medium

 **标签**: 贪心算法、 


------

<h2>861. Score After Flipping Matrix</h2><p>We have a two dimensional matrix&nbsp;<code>A</code> where each value is <code>0</code> or <code>1</code>.</p>

<p>A move consists of choosing any row or column, and toggling each value in that row or column: changing all <code>0</code>s to <code>1</code>s, and all <code>1</code>s to <code>0</code>s.</p>

<p>After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.</p>

<p>Return the highest possible&nbsp;score.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[0,0,1,1],[1,0,1,0],[1,1,0,0]]</span>
<strong>Output: </strong><span id="example-output-1">39</span>
<strong>Explanation:
</strong>Toggled to <span id="example-input-1-1">[[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</span></pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 20</code></li>
	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>
	<li><code>A[i][j]</code>&nbsp;is <code>0</code> or <code>1</code>.</li>
</ol>
</div>


 **difficulty**: Medium

 **topic**: Greedy, 

