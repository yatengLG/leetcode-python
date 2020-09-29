<h2>996. 正方形数组的数目</h2><p>给定一个非负整数数组&nbsp;<code>A</code>，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为<em>正方形</em>数组。</p>

<p>返回 A 的正方形排列的数目。两个排列 <code>A1</code> 和 <code>A2</code> 不同的充要条件是存在某个索引 <code>i</code>，使得 A1[i] != A2[i]。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,17,8]
<strong>输出：</strong>2
<strong>解释：</strong>
[1,8,17] 和 [17,8,1] 都是有效的排列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[2,2,2]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1e9</code></li>
</ol>


 **难度**: Hard

 **标签**: 图、 数学、 回溯算法、 


------

<h2>996. Number of Squareful Arrays</h2><p>Given an array <code>A</code> of non-negative integers, the array is <em>squareful</em> if for every pair of adjacent elements, their sum is a perfect square.</p>

<p>Return the number of permutations of A that are squareful.&nbsp; Two permutations <code>A1</code> and <code>A2</code> differ if and only if there is some index <code>i</code> such that <code>A1[i] != A2[i]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,17,8]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
[1,8,17] and [17,8,1] are the valid permutations.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,2,2]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1e9</code></li>
</ol>

 **difficulty**: Hard

 **topic**: Graph, Math, Backtracking, 

