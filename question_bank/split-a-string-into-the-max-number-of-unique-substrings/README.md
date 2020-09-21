<h2>1593. 拆分字符串使唯一子字符串的数目最大</h2><p>给你一个字符串 <code>s</code> ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。</p>

<p>字符串 <code>s</code> 拆分后可以得到若干 <strong>非空子字符串</strong> ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 <strong>唯一的</strong> 。</p>

<p>注意：<strong>子字符串</strong> 是字符串中的一个连续字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;ababccc&quot;
<strong>输出：</strong>5
<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;b&#39;, &#39;ab&#39;, &#39;c&#39;, &#39;cc&#39;] 。像 [&#39;a&#39;, &#39;b&#39;, &#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;cc&#39;] 这样拆分不满足题目要求，因为其中的 &#39;a&#39; 和 &#39;b&#39; 都出现了不止一次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aba&quot;
<strong>输出：</strong>2
<strong>解释：</strong>一种最大拆分方法为 [&#39;a&#39;, &#39;ba&#39;] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;aa&quot;
<strong>输出：</strong>1
<strong>解释：</strong>无法进一步拆分字符串。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>
	<p><code>1 &lt;= s.length&nbsp;&lt;= 16</code></p>
	</li>
	<li>
	<p><code>s</code> 仅包含小写英文字母</p>
	</li>
</ul>


 **难度**: Medium

 **标签**: 回溯算法、 


------

<h2>1593. Split a String Into the Max Number of Unique Substrings</h2><p>Given a string&nbsp;<code>s</code><var>,</var>&nbsp;return <em>the maximum&nbsp;number of unique substrings that the given string can be split into</em>.</p>

<p>You can split string&nbsp;<code>s</code> into any list of&nbsp;<strong>non-empty substrings</strong>, where the concatenation of the substrings forms the original string.&nbsp;However, you must split the substrings such that all of them are <strong>unique</strong>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababccc&quot;
<strong>Output:</strong> 5
<strong>Explanation</strong>: One way to split maximally is [&#39;a&#39;, &#39;b&#39;, &#39;ab&#39;, &#39;c&#39;, &#39;cc&#39;]. Splitting like [&#39;a&#39;, &#39;b&#39;, &#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;cc&#39;] is not valid as you have &#39;a&#39; and &#39;b&#39; multiple times.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> 2
<strong>Explanation</strong>: One way to split maximally is [&#39;a&#39;, &#39;ba&#39;].
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;
<strong>Output:</strong> 1
<strong>Explanation</strong>: It is impossible to split the string any further.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>
	<p><code>1 &lt;= s.length&nbsp;&lt;= 16</code></p>
	</li>
	<li>
	<p><code>s</code> contains&nbsp;only lower case English letters.</p>
	</li>
</ul>


 **difficulty**: Medium

 **topic**: Backtracking, 

