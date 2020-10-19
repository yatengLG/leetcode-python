<h2>844. 比较含退格的字符串</h2><p>给定 <code>S</code> 和 <code>T</code> 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 <code>#</code> 代表退格字符。</p>

<p><strong>注意：</strong>如果对空文本输入退格字符，文本继续为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = &quot;ab#c&quot;, T = &quot;ad#c&quot;
<strong>输出：</strong>true
<strong>解释：</strong>S 和 T 都会变成 &ldquo;ac&rdquo;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>S = &quot;ab##&quot;, T = &quot;c#d#&quot;
<strong>输出：</strong>true
<strong>解释：</strong>S 和 T 都会变成 &ldquo;&rdquo;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>S = &quot;a##c&quot;, T = &quot;#a#c&quot;
<strong>输出：</strong>true
<strong>解释：</strong>S 和 T 都会变成 &ldquo;c&rdquo;。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>S = &quot;a#c&quot;, T = &quot;b&quot;
<strong>输出：</strong>false
<strong>解释：</strong>S 会变成 &ldquo;c&rdquo;，但 T 仍然是 &ldquo;b&rdquo;。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 200</code></li>
	<li><code>1 &lt;= T.length &lt;= 200</code></li>
	<li><code>S</code> 和 <code>T</code> 只含有小写字母以及字符 <code>&#39;#&#39;</code>。</li>
</ol>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以用 <code>O(N)</code> 的时间复杂度和 <code>O(1)</code> 的空间复杂度解决该问题吗？</li>
</ul>

<p>&nbsp;</p>


 **难度**: Easy

 **标签**: 栈、 双指针、 


------

<h2>844. Backspace String Compare</h2><p>Given two&nbsp;strings&nbsp;<code>S</code>&nbsp;and <code>T</code>,&nbsp;return if they are equal when both are typed into empty text editors. <code>#</code> means a backspace character.</p>

<p>Note that after&nbsp;backspacing an empty text, the text will continue empty.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;ab#c&quot;</span>, T = <span id="example-input-1-2">&quot;ad#c&quot;</span>
<strong>Output: </strong><span id="example-output-1">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;ac&quot;.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;ab##&quot;</span>, T = <span id="example-input-2-2">&quot;c#d#&quot;</span>
<strong>Output: </strong><span id="example-output-2">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;&quot;.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">&quot;a##c&quot;</span>, T = <span id="example-input-3-2">&quot;#a#c&quot;</span>
<strong>Output: </strong><span id="example-output-3">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;c&quot;.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-4-1">&quot;a#c&quot;</span>, T = <span id="example-input-4-2">&quot;b&quot;</span>
<strong>Output: </strong><span id="example-output-4">false
</span><span><strong>Explanation</strong>: S becomes &quot;c&quot; while T becomes &quot;b&quot;.</span>
</pre>

<p><span><strong>Note</strong>:</span></p>

<ul>
	<li><code><span>1 &lt;= S.length &lt;= 200</span></code></li>
	<li><code><span>1 &lt;= T.length &lt;= 200</span></code></li>
	<li><span><code>S</code>&nbsp;and <code>T</code> only contain&nbsp;lowercase letters and <code>&#39;#&#39;</code> characters.</span></li>
</ul>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Can you solve it in <code>O(N)</code> time and <code>O(1)</code> space?</li>
</ul>
</div>
</div>
</div>
</div>


 **difficulty**: Easy

 **topic**: Stack, Two Pointers, 

