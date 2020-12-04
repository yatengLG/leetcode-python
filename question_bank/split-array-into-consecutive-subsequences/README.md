<h2>659. 分割数组为连续子序列</h2><p>给你一个按升序排序的整数数组 <code>num</code>（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。</p>

<p>如果可以完成上述分割，则返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> [1,2,3,3,4,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> [1,2,3,3,4,4,5,5]
<strong>输出:</strong> True
<strong>解释:</strong>
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5
</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre><strong>输入:</strong> [1,2,3,4,4,5]
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>输入的数组长度范围为 [1, 10000]</li>
</ol>

<p>&nbsp;</p>


 **难度**: Medium

 **标签**: 堆、 贪心算法、 


------

<h2>659. Split Array into Consecutive Subsequences</h2><p>Given an array <code>nums</code>&nbsp;sorted in ascending order, return <code>true</code> if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers&nbsp;and has length at least 3.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,2,3,3,4,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1,2,3,3,4,4,5,5]
<b>Output:</b> True
<b>Explanation:</b>
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> [1,2,3,4,4,5]
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Constraints:</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10000</code></li>
</ul>

<p>&nbsp;</p>


 **difficulty**: Medium

 **topic**: Heap, Greedy, 

