<h2>303. 区域和检索 - 数组不可变</h2><p>给定一个整数数组 &nbsp;<em>nums</em>，求出数组从索引&nbsp;<em>i&nbsp;</em>到&nbsp;<em>j&nbsp;&nbsp;</em>(<em>i</em>&nbsp;&le;&nbsp;<em>j</em>) 范围内元素的总和，包含&nbsp;<em>i,&nbsp; j&nbsp;</em>两点。</p>

<p><strong>示例：</strong></p>

<pre>给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -&gt; 1
sumRange(2, 5) -&gt; -1
sumRange(0, 5) -&gt; -3</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>你可以假设数组不可变。</li>
	<li>会多次调用&nbsp;<em>sumRange</em>&nbsp;方法。</li>
</ol>


 **难度**: Easy

 **标签**: 动态规划、 


------

<h2>303. Range Sum Query - Immutable</h2><p>Given an integer array <i>nums</i>, find the sum of the elements between indices <i>i</i> and <i>j</i> (<i>i</i> &le; <i>j</i>), inclusive.</p>

<p><b>Example:</b></p>

<pre>
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -&gt; 1
sumRange(2, 5) -&gt; -1
sumRange(0, 5) -&gt; -3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>You may assume that the array does not change.</li>
	<li>There are many calls to <i>sumRange</i> function.</li>
	<li><code>0 &lt;= nums.length &lt;= 10^4</code></li>
	<li><code>-10^5&nbsp;&lt;= nums[i] &lt;=&nbsp;10^5</code></li>
	<li><code>0 &lt;= i &lt;= j &lt; nums.length</code></li>
</ul>


 **difficulty**: Easy

 **topic**: Dynamic Programming, 

