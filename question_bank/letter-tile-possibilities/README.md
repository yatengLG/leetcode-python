<h2>1079. 活字印刷</h2><p>你有一套活字字模&nbsp;<code>tiles</code>，其中每个字模上都刻有一个字母&nbsp;<code>tiles[i]</code>。返回你可以印出的非空字母序列的数目。</p>

<p><strong>注意：</strong>本题中，每个活字字模只能使用一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>&quot;AAB&quot;
<strong>输出：</strong>8
<strong>解释：</strong>可能的序列为 &quot;A&quot;, &quot;B&quot;, &quot;AA&quot;, &quot;AB&quot;, &quot;BA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;BAA&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>&quot;AAABBC&quot;
<strong>输出：</strong>188
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= tiles.length &lt;= 7</code></li>
	<li><code>tiles</code> 由大写英文字母组成</li>
</ol>


 **难度**: Medium

 **标签**: 回溯算法、 


------

<h2>1079. Letter Tile Possibilities</h2><p>You have <code>n</code>&nbsp;&nbsp;<code>tiles</code>, where each tile has one letter <code>tiles[i]</code> printed on it.</p>

<p>Return <em>the number of possible non-empty sequences of letters</em> you can make using the letters printed on those <code>tiles</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;AAB&quot;
<strong>Output:</strong> 8
<strong>Explanation: </strong>The possible sequences are &quot;A&quot;, &quot;B&quot;, &quot;AA&quot;, &quot;AB&quot;, &quot;BA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;BAA&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;AAABBC&quot;
<strong>Output:</strong> 188
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> tiles = &quot;V&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= tiles.length &lt;= 7</code></li>
	<li><code>tiles</code> consists of uppercase English letters.</li>
</ul>


 **difficulty**: Medium

 **topic**: Backtracking, 

