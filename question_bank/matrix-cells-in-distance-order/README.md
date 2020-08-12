<h2>1030. 距离顺序排列矩阵单元格</h2><p>给出 <code>R</code> 行 <code>C</code> 列的矩阵，其中的单元格的整数坐标为 <code>(r, c)</code>，满足 <code>0 &lt;= r &lt; R</code> 且 <code>0 &lt;= c &lt; C</code>。</p>

<p>另外，我们在该矩阵中给出了一个坐标为&nbsp;<code>(r0, c0)</code> 的单元格。</p>

<p>返回矩阵中的所有单元格的坐标，并按到 <code>(r0, c0)</code> 的距离从最小到最大的顺序排，其中，两单元格<code>(r1, c1)</code> 和 <code>(r2, c2)</code> 之间的距离是曼哈顿距离，<code>|r1 - r2| + |c1 - c2|</code>。（你可以按任何满足此条件的顺序返回答案。）</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>R = 1, C = 2, r0 = 0, c0 = 0
<strong>输出：</strong>[[0,0],[0,1]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>R = 2, C = 2, r0 = 0, c0 = 1
<strong>输出：</strong>[[0,1],[0,0],[1,1],[1,0]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>R = 2, C = 3, r0 = 1, c0 = 2
<strong>输出：</strong>[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
<strong>解释</strong>：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= R &lt;= 100</code></li>
	<li><code>1 &lt;= C &lt;= 100</code></li>
	<li><code>0 &lt;= r0 &lt; R</code></li>
	<li><code>0 &lt;= c0 &lt; C</code></li>
</ol>
 **难度**: Easy

 **标签**: 排序、 


------

<h2>1030. Matrix Cells in Distance Order</h2><p>We are given a matrix with <code>R</code> rows and <code>C</code> columns has cells with integer coordinates&nbsp;<code>(r, c)</code>, where <code>0 &lt;= r &lt; R</code> and <code>0 &lt;= c &lt; C</code>.</p>

<p>Additionally, we are given a cell in that matrix with coordinates&nbsp;<code>(r0, c0)</code>.</p>

<p>Return the coordinates of&nbsp;all cells in the matrix, sorted by their distance from <code>(r0, c0)</code>&nbsp;from smallest distance to largest distance.&nbsp; Here,&nbsp;the distance between two cells <code>(r1, c1)</code> and <code>(r2, c2)</code> is the Manhattan distance,&nbsp;<code>|r1 - r2| + |c1 - c2|</code>.&nbsp; (You may return the answer in any order that satisfies this condition.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-1-1">1</span>, C = <span id="example-input-1-2">2</span>, r0 = <span id="example-input-1-3">0</span>, c0 = <span id="example-input-1-4">0</span>
<strong>Output: </strong><span id="example-output-1">[[0,0],[0,1]]
<strong>Explanation:</strong> The distances from (r0, c0) to other cells are: [0,1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-2-1">2</span>, C = <span id="example-input-2-2">2</span>, r0 = <span id="example-input-2-3">0</span>, c0 = <span id="example-input-2-4">1</span>
<strong>Output: </strong><span id="example-output-2">[[0,1],[0,0],[1,1],[1,0]]
</span><span id="example-output-1"><strong>Explanation:</strong> The distances from (r0, c0) to other cells are:</span><span> [0,1,1,2]</span>
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>R = <span id="example-input-3-1">2</span>, C = <span id="example-input-3-2">3</span>, r0 = <span id="example-input-3-3">1</span>, c0 = <span id="example-input-3-4">2</span>
<strong>Output: </strong><span id="example-output-3">[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]</span>
<span id="example-output-1"><strong>Explanation:</strong> The distances from (r0, c0) to other cells are:</span><span> [0,1,1,2,2,3]</span>
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= R &lt;= 100</code></li>
	<li><code>1 &lt;= C &lt;= 100</code></li>
	<li><code>0 &lt;= r0 &lt; R</code></li>
	<li><code>0 &lt;= c0 &lt; C</code></li>
</ol>
</div>
</div>
</div>
 **difficulty**: Easy

 **topic**: Sort, 

