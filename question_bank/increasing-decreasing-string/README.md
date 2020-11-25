<h2>1370. 上升下降字符串</h2><p>给你一个字符串&nbsp;<code>s</code>&nbsp;，请你根据下面的算法重新构造字符串：</p>

<ol>
	<li>从 <code>s</code>&nbsp;中选出 <strong>最小</strong>&nbsp;的字符，将它 <strong>接在</strong>&nbsp;结果字符串的后面。</li>
	<li>从 <code>s</code>&nbsp;剩余字符中选出&nbsp;<strong>最小</strong>&nbsp;的字符，且该字符比上一个添加的字符大，将它 <strong>接在</strong>&nbsp;结果字符串后面。</li>
	<li>重复步骤 2 ，直到你没法从 <code>s</code>&nbsp;中选择字符。</li>
	<li>从 <code>s</code>&nbsp;中选出 <strong>最大</strong>&nbsp;的字符，将它 <strong>接在</strong>&nbsp;结果字符串的后面。</li>
	<li>从 <code>s</code>&nbsp;剩余字符中选出&nbsp;<strong>最大</strong>&nbsp;的字符，且该字符比上一个添加的字符小，将它 <strong>接在</strong>&nbsp;结果字符串后面。</li>
	<li>重复步骤 5&nbsp;，直到你没法从 <code>s</code>&nbsp;中选择字符。</li>
	<li>重复步骤 1 到 6 ，直到 <code>s</code>&nbsp;中所有字符都已经被选过。</li>
</ol>

<p>在任何一步中，如果最小或者最大字符不止一个&nbsp;，你可以选择其中任意一个，并将其添加到结果字符串。</p>

<p>请你返回将&nbsp;<code>s</code>&nbsp;中字符重新排序后的 <strong>结果字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaaabbbbcccc&quot;
<strong>输出：</strong>&quot;abccbaabccba&quot;
<strong>解释：</strong>第一轮的步骤 1，2，3 后，结果字符串为 result = &quot;abc&quot;
第一轮的步骤 4，5，6 后，结果字符串为 result = &quot;abccba&quot;
第一轮结束，现在 s = &quot;aabbcc&quot; ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = &quot;abccbaabc&quot;
第二轮的步骤 4，5，6 后，结果字符串为 result = &quot;abccbaabccba&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;rat&quot;
<strong>输出：</strong>&quot;art&quot;
<strong>解释：</strong>单词 &quot;rat&quot; 在上述算法重排序以后变成 &quot;art&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;leetcode&quot;
<strong>输出：</strong>&quot;cdelotee&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;ggggggg&quot;
<strong>输出：</strong>&quot;ggggggg&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;spo&quot;
<strong>输出：</strong>&quot;ops&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


 **难度**: Easy

 **标签**: 排序、 字符串、 


------

<h2>1370. Increasing Decreasing String</h2><p>Given a string <code>s</code>. You should re-order the string using the following algorithm:</p>

<ol>
	<li>Pick the <strong>smallest</strong> character from <code>s</code> and <strong>append</strong> it to the result.</li>
	<li>Pick the <strong>smallest</strong> character from <code>s</code> which is greater than the last appended character to the result and <strong>append</strong> it.</li>
	<li>Repeat step 2 until you cannot pick more characters.</li>
	<li>Pick the <strong>largest</strong>&nbsp;character from <code>s</code> and <strong>append</strong> it to the result.</li>
	<li>Pick the <strong>largest</strong>&nbsp;character from <code>s</code> which is smaller than the last appended character to the result and <strong>append</strong> it.</li>
	<li>Repeat step 5 until you cannot pick more characters.</li>
	<li>Repeat the steps from 1 to 6 until you pick all characters from <code>s</code>.</li>
</ol>

<p>In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.</p>

<p>Return <em>the result string</em> after sorting <code>s</code>&nbsp;with this algorithm.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaaabbbbcccc&quot;
<strong>Output:</strong> &quot;abccbaabccba&quot;
<strong>Explanation:</strong> After steps 1, 2 and 3 of the first iteration, result = &quot;abc&quot;
After steps 4, 5 and 6 of the first iteration, result = &quot;abccba&quot;
First iteration is done. Now s = &quot;aabbcc&quot; and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = &quot;abccbaabc&quot;
After steps 4, 5 and 6 of the second iteration, result = &quot;abccbaabccba&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rat&quot;
<strong>Output:</strong> &quot;art&quot;
<strong>Explanation:</strong> The word &quot;rat&quot; becomes &quot;art&quot; after re-ordering it with the mentioned algorithm.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;
<strong>Output:</strong> &quot;cdelotee&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ggggggg&quot;
<strong>Output:</strong> &quot;ggggggg&quot;
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;spo&quot;
<strong>Output:</strong> &quot;ops&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> contains only lower-case English letters.</li>
</ul>


 **difficulty**: Easy

 **topic**: Sort, String, 

