<h2>845. 数组中的最长山脉</h2><p>我们把数组 A 中符合下列属性的任意连续子数组 B 称为 &ldquo;<em>山脉&rdquo;</em>：</p>

<ul>
	<li><code>B.length &gt;= 3</code></li>
	<li>存在 <code>0 &lt; i&nbsp;&lt; B.length - 1</code> 使得 <code>B[0] &lt; B[1] &lt; ... B[i-1] &lt; B[i] &gt; B[i+1] &gt; ... &gt; B[B.length - 1]</code></li>
</ul>

<p>（注意：B 可以是 A 的任意子数组，包括整个数组 A。）</p>

<p>给出一个整数数组 <code>A</code>，返回最长 <em>&ldquo;山脉&rdquo;</em>&nbsp;的长度。</p>

<p>如果不含有 &ldquo;<em>山脉&rdquo;&nbsp;</em>则返回 <code>0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[2,1,4,7,3,2,5]
<strong>输出：</strong>5
<strong>解释：</strong>最长的 &ldquo;山脉&rdquo; 是 [1,4,7,3,2]，长度为 5。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[2,2,2]
<strong>输出：</strong>0
<strong>解释：</strong>不含 &ldquo;山脉&rdquo;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
</ol>


 **难度**: Medium

 **标签**: 双指针、 


------

<h2>845. Longest Mountain in Array</h2><p>Let&#39;s call any (contiguous) subarray B (of A)&nbsp;a <em>mountain</em> if the following properties hold:</p>

<ul>
	<li><code>B.length &gt;= 3</code></li>
	<li>There exists some <code>0 &lt; i&nbsp;&lt; B.length - 1</code> such that <code>B[0] &lt; B[1] &lt; ... B[i-1] &lt; B[i] &gt; B[i+1] &gt; ... &gt; B[B.length - 1]</code></li>
</ul>

<p>(Note that B could be any subarray of A, including the entire array A.)</p>

<p>Given an array <code>A</code>&nbsp;of integers,&nbsp;return the length of the longest&nbsp;<em>mountain</em>.&nbsp;</p>

<p>Return <code>0</code> if there is no mountain.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[2,1,4,7,3,2,5]
<strong>Output: </strong>5
<strong>Explanation: </strong>The largest mountain is [1,4,7,3,2] which has length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[2,2,2]
<strong>Output: </strong>0
<strong>Explanation: </strong>There is no mountain.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
</ol>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Can you solve it using only one pass?</li>
	<li>Can you solve it in <code>O(1)</code> space?</li>
</ul>


 **difficulty**: Medium

 **topic**: Two Pointers, 

