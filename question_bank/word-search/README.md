<h2>79. 单词搜索</h2><p>给定一个二维网格和一个单词，找出该单词是否存在于网格中。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中&ldquo;相邻&rdquo;单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

给定 word = &quot;<strong>ABCCED</strong>&quot;, 返回 <strong>true</strong>
给定 word = &quot;<strong>SEE</strong>&quot;, 返回 <strong>true</strong>
给定 word = &quot;<strong>ABCB</strong>&quot;, 返回 <strong>false</strong></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>board</code> 和 <code>word</code> 中只包含大写和小写英文字母。</li>
	<li><code>1 &lt;= board.length &lt;= 200</code></li>
	<li><code>1 &lt;= board[i].length &lt;= 200</code></li>
	<li><code>1 &lt;= word.length &lt;= 10^3</code></li>
</ul>


 **难度**: Medium

 **标签**: 数组、 回溯算法、 


------

<h2>79. Word Search</h2><p>Given a 2D board and a word, find if the word exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cell, where &quot;adjacent&quot; cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p><strong>Example:</strong></p>

<pre>
board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

Given word = &quot;<strong>ABCCED</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>SEE</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>ABCB</strong>&quot;, return <strong>false</strong>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board</code>&nbsp;and <code>word</code> consists only of lowercase and uppercase English letters.</li>
	<li><code>1 &lt;= board.length &lt;= 200</code></li>
	<li><code>1 &lt;= board[i].length &lt;= 200</code></li>
	<li><code>1 &lt;= word.length &lt;= 10^3</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Array, Backtracking, 

