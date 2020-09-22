<h2>1441. 用栈操作构建数组</h2><p>给你一个目标数组 <code>target</code> 和一个整数 <code>n</code>。每次迭代，需要从&nbsp; <code>list = {1,2,3..., n}</code> 中依序读取一个数字。</p>

<p>请使用下述操作来构建目标数组 <code>target</code> ：</p>

<ul>
	<li><strong>Push</strong>：从 <code>list</code> 中读取一个新元素， 并将其推入数组中。</li>
	<li><strong>Pop</strong>：删除数组中的最后一个元素。</li>
	<li>如果目标数组构建完成，就停止读取更多元素。</li>
</ul>

<p>题目数据保证目标数组严格递增，并且只包含 <code>1</code> 到 <code>n</code> 之间的数字。</p>

<p>请返回构建目标数组所用的操作序列。</p>

<p>题目数据保证答案是唯一的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = [1,3], n = 3
<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;]
<strong>解释： 
</strong>读取 1 并自动推入数组 -&gt; [1]
读取 2 并自动推入数组，然后删除它 -&gt; [1]
读取 3 并自动推入数组 -&gt; [1,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = [1,2,3], n = 3
<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = [1,2], n = 4
<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;]
<strong>解释：</strong>只需要读取前 2 个数字就可以停止。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>target = [2,3,4], n = 4
<strong>输出：</strong>[&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= target[i]&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>target</code> 是严格递增的</li>
</ul>


 **难度**: Easy

 **标签**: 栈、 


------

<h2>1441. Build an Array With Stack Operations</h2><p>Given an array <code>target</code> and&nbsp;an integer <code>n</code>. In each iteration, you will read a number from &nbsp;<code>list = {1,2,3..., n}</code>.</p>

<p>Build the <code>target</code>&nbsp;array&nbsp;using the following operations:</p>

<ul>
	<li><strong>Push</strong>: Read a new element from the beginning&nbsp;<code>list</code>, and push it in the array.</li>
	<li><strong>Pop</strong>: delete the last element of&nbsp;the array.</li>
	<li>If the target array is already&nbsp;built, stop reading more elements.</li>
</ul>

<p>You are guaranteed that the target array is strictly&nbsp;increasing, only containing&nbsp;numbers between 1 to <code>n</code>&nbsp;inclusive.</p>

<p>Return the operations to build the target array.</p>

<p>You are guaranteed that the answer is unique.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [1,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;]
<strong>Explanation: 
</strong>Read number 1 and automatically push in the array -&gt; [1]
Read number 2 and automatically push in the array then Pop it -&gt; [1]
Read number 3 and automatically push in the array -&gt; [1,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2,3], n = 3
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2], n = 4
<strong>Output:</strong> [&quot;Push&quot;,&quot;Push&quot;]
<strong>Explanation: </strong>You only need to read the first 2 numbers and stop.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> target = [2,3,4], n = 4
<strong>Output:</strong> [&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= target[i]&nbsp;&lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>target</code> is strictly&nbsp;increasing.</li>
</ul>


 **difficulty**: Easy

 **topic**: Stack, 

