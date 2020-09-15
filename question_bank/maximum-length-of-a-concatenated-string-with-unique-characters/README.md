<h2>1239. 串联字符串的最大长度</h2><p>给定一个字符串数组 <code>arr</code>，字符串 <code>s</code> 是将 <code>arr</code> 某一子序列字符串连接所得的字符串，如果 <code>s</code> 中的每一个字符都只出现过一次，那么它就是一个可行解。</p>

<p>请返回所有可行解 <code>s</code> 中最长长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;]
<strong>输出：</strong>4
<strong>解释：</strong>所有可能的串联组合是 &quot;&quot;,&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;,&quot;uniq&quot; 和 &quot;ique&quot;，最大长度为 4。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [&quot;cha&quot;,&quot;r&quot;,&quot;act&quot;,&quot;ers&quot;]
<strong>输出：</strong>6
<strong>解释：</strong>可能的解答有 &quot;chaers&quot; 和 &quot;acters&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [&quot;abcdefghijklmnopqrstuvwxyz&quot;]
<strong>输出：</strong>26
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 16</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 26</code></li>
	<li><code>arr[i]</code>&nbsp;中只含有小写英文字母</li>
</ul>


 **难度**: Medium

 **标签**: 位运算、 回溯算法、 


------

<h2>1239. Maximum Length of a Concatenated String with Unique Characters</h2><p>Given an array of strings <code>arr</code>. String <code>s</code> is a concatenation of a sub-sequence of <code>arr</code> which have <strong>unique characters</strong>.</p>

<p>Return <em>the maximum possible length</em> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All possible concatenations are &quot;&quot;,&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;,&quot;uniq&quot; and &quot;ique&quot;.
Maximum length is 4.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [&quot;cha&quot;,&quot;r&quot;,&quot;act&quot;,&quot;ers&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Possible solutions are &quot;chaers&quot; and &quot;acters&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [&quot;abcdefghijklmnopqrstuvwxyz&quot;]
<strong>Output:</strong> 26
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 16</code></li>
	<li><code>1 &lt;= arr[i].length &lt;= 26</code></li>
	<li><code>arr[i]</code> contains only lower case English letters.</li>
</ul>


 **difficulty**: Medium

 **topic**: Bit Manipulation, Backtracking, 

