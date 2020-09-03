<h2>1566. 重复至少 K 次且长度为 M 的模式</h2><p>给你一个正整数数组 <code>arr</code>，请你找出一个长度为 <code>m</code> 且在数组中至少重复 <code>k</code> 次的模式。</p>

<p><strong>模式</strong> 是由一个或多个值组成的子数组（连续的子序列），<strong>连续</strong> 重复多次但 <strong>不重叠</strong> 。 模式由其长度和重复次数定义。</p>

<p>如果数组中存在至少重复 <code>k</code> 次且长度为 <code>m</code> 的模式，则返回 <code>true</code> ，否则返回&nbsp; <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,4,4,4,4], m = 1, k = 3
<strong>输出：</strong>true
<strong>解释：</strong>模式 <strong>(4)</strong> 的长度为 1 ，且连续重复 4 次。注意，模式可以重复 k 次或更多次，但不能少于 k 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
<strong>输出：</strong>true
<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，且连续重复 2 次。另一个符合题意的模式是 <strong>(2,1) </strong>，同样重复 2 次。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,1,2,1,3], m = 2, k = 3
<strong>输出：</strong>false
<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，但是只连续重复 2 次。不存在长度为 2 且至少重复 3 次的模式。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,3,1,2], m = 2, k = 2
<strong>输出：</strong>false
<strong>解释：</strong>模式 <strong>(1,2)</strong> 出现 2 次但并不连续，所以不能算作连续重复 2 次。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [2,2,2,2], m = 2, k = 3
<strong>输出：</strong>false
<strong>解释：</strong>长度为 2 的模式只有 <strong>(2,2)</strong> ，但是只连续重复 2 次。注意，不能计算重叠的重复次数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;= 100</code></li>
	<li><code>2 &lt;= k&nbsp;&lt;= 100</code></li>
</ul>


 **难度**: Easy

 **标签**: 数组、 


------

<h2>1566. Detect Pattern of Length M Repeated K or More Times</h2><p>Given an array of positive integers <code>arr</code>,&nbsp; find a pattern of length <code>m</code> that is repeated <code>k</code> or more times.</p>

<p>A <strong>pattern</strong> is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times <strong>consecutively </strong>without overlapping. A pattern is defined by its length and the number of repetitions.</p>

<p>Return&nbsp;<code>true</code>&nbsp;<em>if there exists a pattern of length</em>&nbsp;<code>m</code>&nbsp;<em>that is repeated</em>&nbsp;<code>k</code>&nbsp;<em>or more times, otherwise return</em>&nbsp;<code>false</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,4,4,4,4], m = 1, k = 3
<strong>Output:</strong> true
<strong>Explanation: </strong>The pattern <strong>(4)</strong> of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
<strong>Output:</strong> true
<strong>Explanation: </strong>The pattern <strong>(1,2)</strong> of length 2 is repeated 2 consecutive times. Another valid pattern <strong>(2,1) is</strong> also repeated 2 times.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,1,2,1,3], m = 2, k = 3
<strong>Output:</strong> false
<strong>Explanation: </strong>The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,1,2], m = 2, k = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Notice that the pattern (1,2) exists twice but not consecutively, so it doesn&#39;t count.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,2,2,2], m = 2, k = 3
<strong>Output:</strong> false
<strong>Explanation: </strong>The only pattern of length 2 is (2,2) however it&#39;s repeated only twice. Notice that we do not count overlapping repetitions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;= 100</code></li>
	<li><code>2 &lt;= k&nbsp;&lt;= 100</code></li>
</ul>


 **difficulty**: Easy

 **topic**: Array, 

