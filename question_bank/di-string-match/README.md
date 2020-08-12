<h2>942. 增减字符串匹配</h2><p>给定只含&nbsp;<code>&quot;I&quot;</code>（增大）或 <code>&quot;D&quot;</code>（减小）的字符串&nbsp;<code>S</code>&nbsp;，令&nbsp;<code>N = S.length</code>。</p>

<p>返回&nbsp;<code>[0, 1, ..., N]</code>&nbsp;的任意排列&nbsp;<code>A</code>&nbsp;使得对于所有&nbsp;<code>i = 0,&nbsp;..., N-1</code>，都有：</p>

<ul>
	<li>如果&nbsp;<code>S[i] == &quot;I&quot;</code>，那么&nbsp;<code>A[i] &lt; A[i+1]</code></li>
	<li>如果&nbsp;<code>S[i] == &quot;D&quot;</code>，那么&nbsp;<code>A[i] &gt; A[i+1]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输出：</strong>&quot;IDID&quot;
<strong>输出：</strong>[0,4,1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输出：</strong>&quot;III&quot;
<strong>输出：</strong>[0,1,2,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输出：</strong>&quot;DDI&quot;
<strong>输出：</strong>[3,2,0,1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 10000</code></li>
	<li><code>S</code> 只包含字符&nbsp;<code>&quot;I&quot;</code>&nbsp;或&nbsp;<code>&quot;D&quot;</code>。</li>
</ol>
 难度: Easy

 标签: 数学、 


------

<h2>942. DI String Match</h2><p>Given a string <code>S</code> that <strong>only</strong> contains &quot;I&quot; (increase) or &quot;D&quot; (decrease), let <code>N = S.length</code>.</p>

<p>Return <strong>any</strong> permutation <code>A</code> of <code>[0, 1, ..., N]</code> such that for all <code>i = 0,&nbsp;..., N-1</code>:</p>

<ul>
	<li>If <code>S[i] == &quot;I&quot;</code>, then <code>A[i] &lt; A[i+1]</code></li>
	<li>If <code>S[i] == &quot;D&quot;</code>, then <code>A[i] &gt; A[i+1]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;IDID&quot;</span>
<strong>Output: </strong><span id="example-output-1">[0,4,1,3,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;III&quot;</span>
<strong>Output: </strong><span id="example-output-2">[0,1,2,3]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;DDI&quot;</span>
<strong>Output: </strong><span id="example-output-3">[3,2,0,1]</span></pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 10000</code></li>
	<li><code>S</code> only contains characters <code>&quot;I&quot;</code> or <code>&quot;D&quot;</code>.</li>
</ol>
------

 difficulty: Easy

 topic: Math, 

