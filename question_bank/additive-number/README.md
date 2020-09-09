<h2>306. 累加数</h2><p>累加数是一个字符串，组成它的数字可以形成累加序列。</p>

<p>一个有效的累加序列必须<strong>至少</strong>包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。</p>

<p>给定一个只包含数字&nbsp;<code>&#39;0&#39;-&#39;9&#39;</code>&nbsp;的字符串，编写一个算法来判断给定输入是否是累加数。</p>

<p><strong>说明:&nbsp;</strong>累加序列里的数不会以 0 开头，所以不会出现&nbsp;<code>1, 2, 03</code> 或者&nbsp;<code>1, 02, 3</code>&nbsp;的情况。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>&quot;112358&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 1, 2, 3, 5, 8 </code>。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>&quot;199100199&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 99, 100, 199。</code>1 + 99 = 100, 99 + 100 = 199</pre>

<p><strong>进阶:</strong><br>
你如何处理一个溢出的过大的整数输入?</p>


 **难度**: Medium

 **标签**: 回溯算法、 


------

<h2>306. Additive Number</h2><p>Additive number is a string whose digits can form additive sequence.</p>

<p>A valid additive sequence should contain <b>at least</b> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

<p>Given a string containing only digits <code>&#39;0&#39;-&#39;9&#39;</code>, write a function to determine if it&#39;s an additive number.</p>

<p><b>Note:</b> Numbers in the additive sequence <b>cannot</b> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;112358&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
&nbsp;            1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;199100199&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The additive sequence is: 1, 99, 100, 199.&nbsp;
&nbsp;            1 + 99 = 100, 99 + 100 = 199
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><font face="monospace"><code>num</code>&nbsp;</font>consists only of digits <code>&#39;0&#39;-&#39;9&#39;</code>.</li>
	<li><code>1 &lt;= num.length &lt;= 35</code></li>
</ul>

<p><b>Follow up:</b><br />
How would you handle overflow for very large input integers?</p>


 **difficulty**: Medium

 **topic**: Backtracking, 

