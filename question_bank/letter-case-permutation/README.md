<h2>784. 字母大小写全排列</h2><p>给定一个字符串<code>S</code>，通过将字符串<code>S</code>中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。</p>

<p>&nbsp;</p>

<pre><strong>示例：</strong>
<strong>输入：</strong>S = &quot;a1b2&quot;
<strong>输出：</strong>[&quot;a1b2&quot;, &quot;a1B2&quot;, &quot;A1b2&quot;, &quot;A1B2&quot;]

<strong>输入：</strong>S = &quot;3z4&quot;
<strong>输出：</strong>[&quot;3z4&quot;, &quot;3Z4&quot;]

<strong>输入：</strong>S = &quot;12345&quot;
<strong>输出：</strong>[&quot;12345&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>S</code>&nbsp;的长度不超过<code>12</code>。</li>
	<li><code>S</code>&nbsp;仅由数字和字母组成。</li>
</ul>


 **难度**: Medium

 **标签**: 位运算、 回溯算法、 


------

<h2>784. Letter Case Permutation</h2><p>Given a string S, we can transform every letter individually&nbsp;to be lowercase or uppercase to create another string.</p>

<p>Return <em>a list of all possible strings we could create</em>. You can return the output&nbsp;in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;a1b2&quot;
<strong>Output:</strong> [&quot;a1b2&quot;,&quot;a1B2&quot;,&quot;A1b2&quot;,&quot;A1B2&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;3z4&quot;
<strong>Output:</strong> [&quot;3z4&quot;,&quot;3Z4&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;12345&quot;
<strong>Output:</strong> [&quot;12345&quot;]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;0&quot;
<strong>Output:</strong> [&quot;0&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>S</code> will be a string with length between <code>1</code> and <code>12</code>.</li>
	<li><code>S</code> will consist only of letters or digits.</li>
</ul>


 **difficulty**: Medium

 **topic**: Bit Manipulation, Backtracking, 

