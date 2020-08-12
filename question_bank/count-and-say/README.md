<h2>38. 外观数列</h2><p>给定一个正整数 <em>n</em>（1 &le;&nbsp;<em>n</em>&nbsp;&le; 30），输出外观数列的第 <em>n</em> 项。</p>

<p>注意：整数序列中的每一项将表示为一个字符串。</p>

<p>「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：</p>

<pre>1.     1
2.     11
3.     21
4.     1211
5.     111221
</pre>

<p>第一项是数字 1</p>

<p>描述前一项，这个数是 <code>1</code> 即 &ldquo;一个 1 &rdquo;，记作 <code>11</code></p>

<p>描述前一项，这个数是 <code>11</code> 即 &ldquo;两个 1 &rdquo; ，记作 <code>21</code></p>

<p>描述前一项，这个数是 <code>21</code> 即 &ldquo;一个 2 一个 1 &rdquo; ，记作 <code>1211</code></p>

<p>描述前一项，这个数是 <code>1211</code> 即 &ldquo;一个 1 一个 2 两个 1 &rdquo; ，记作 <code>111221</code></p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 1
<strong>输出:</strong> &quot;1&quot;
<strong>解释：</strong>这是一个基本样例。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 4
<strong>输出:</strong> &quot;1211&quot;
<strong>解释：</strong>当 n = 3 时，序列是 &quot;21&quot;，其中我们有 &quot;2&quot; 和 &quot;1&quot; 两组，&quot;2&quot; 可以读作 &quot;12&quot;，也就是出现频次 = 1 而 值 = 2；类似 &quot;1&quot; 可以读作 &quot;11&quot;。所以答案是 &quot;12&quot; 和 &quot;11&quot; 组合在一起，也就是 &quot;1211&quot;。</pre>

------

 难度: Easy

 标签: 字符串、 

<h2>38. Count and Say</h2><p>The count-and-say sequence is the sequence of integers with the first five terms as following:</p>

<pre>
1.     1
2.     11
3.     21
4.     1211
5.     111221
</pre>

<p><code>1</code> is read off as <code>&quot;one 1&quot;</code> or <code>11</code>.<br />
<code>11</code> is read off as <code>&quot;two 1s&quot;</code> or <code>21</code>.<br />
<code>21</code> is read off as <code>&quot;one 2</code>, then <code>one 1&quot;</code> or <code>1211</code>.</p>

<p>Given an integer <i>n</i>&nbsp;where 1 &le; <em>n</em> &le; 30, generate the <i>n</i><sup>th</sup> term of the count-and-say sequence. You can do so recursively, in other words from the previous member&nbsp;read off the digits, counting the number of digits in groups of the same digit.</p>

<p>Note: Each term of the sequence of integers will be represented as a string.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 1
<b>Output:</b> &quot;1&quot;
<b>Explanation:</b> This is the base case.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 4
<b>Output:</b> &quot;1211&quot;
<b>Explanation:</b> For n = 3 the term was &quot;21&quot; in which we have two groups &quot;2&quot; and &quot;1&quot;, &quot;2&quot; can be read as &quot;12&quot; which means frequency = 1 and value = 2, the same way &quot;1&quot; is read as &quot;11&quot;, so the answer is the concatenation of &quot;12&quot; and &quot;11&quot; which is &quot;1211&quot;.
</pre>

------

 difficulty: Easy

 topic: String, 

