<h2>392. 判断子序列</h2><p>给定字符串 <strong>s</strong> 和 <strong>t</strong> ，判断 <strong>s</strong> 是否为 <strong>t</strong> 的子序列。</p>

<p>你可以认为 <strong>s</strong> 和 <strong>t</strong> 中仅包含英文小写字母。字符串 <strong>t</strong> 可能会很长（长度 ~= 500,000），而 <strong>s</strong> 是个短字符串（长度 &lt;=100）。</p>

<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，<code>&quot;ace&quot;</code>是<code>&quot;abcde&quot;</code>的一个子序列，而<code>&quot;aec&quot;</code>不是）。</p>

<p><strong>示例&nbsp;1:</strong><br />
<strong>s</strong> = <code>&quot;abc&quot;</code>, <strong>t</strong> = <code>&quot;ahbgdc&quot;</code></p>

<p>返回&nbsp;<code>true</code>.</p>

<p><strong>示例&nbsp;2:</strong><br />
<strong>s</strong> = <code>&quot;axc&quot;</code>, <strong>t</strong> = <code>&quot;ahbgdc&quot;</code></p>

<p>返回&nbsp;<code>false</code>.</p>

<p><strong>后续挑战</strong> <strong>:</strong></p>

<p>如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k &gt;= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？</p>

<p><strong>致谢:</strong></p>

<p>特别感谢<strong> </strong><a href="https://leetcode.com/pbrother/">@pbrother&nbsp;</a>添加此问题并且创建所有测试用例。</p>


 **难度**: Easy

 **标签**: 贪心算法、 二分查找、 动态规划、 


------

<h2>392. Is Subsequence</h2><p>Given a string <b>s</b> and a string <b>t</b>, check if <b>s</b> is subsequence of <b>t</b>.</p>

<p>A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;abcde&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p><b>Follow up:</b><br />
If there are lots of incoming S, say S1, S2, ... , Sk where k &gt;= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?</p>

<p><b>Credits:</b><br />
Special thanks to <a href="https://leetcode.com/pbrother/">@pbrother</a> for adding this problem and creating all test cases.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10^4</code></li>
	<li>Both strings consists only of lowercase characters.</li>
</ul>


 **difficulty**: Easy

 **topic**: Greedy, Binary Search, Dynamic Programming, 

