<h2>763. 划分字母区间</h2><p>字符串 <code>S</code> 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>S = &quot;ababcbacadefegdehijhklij&quot;
<strong>输出：</strong>[9,7,8]
<strong>解释：</strong>
划分结果为 &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;。
每个字母最多出现在一个片段中。
像 &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; 的划分是错误的，因为划分的片段数较少。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>S</code>的长度在<code>[1, 500]</code>之间。</li>
	<li><code>S</code>只包含小写字母 <code>&#39;a&#39;</code> 到 <code>&#39;z&#39;</code> 。</li>
</ul>


 **难度**: Medium

 **标签**: 贪心算法、 双指针、 


------

<h2>763. Partition Labels</h2><p>A string <code>S</code> of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> S = &quot;ababcbacadefegdehijhklij&quot;
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;.
This is a partition so that each letter appears in at most one part.
A partition like &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; is incorrect, because it splits S into less parts.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
	<li><code>S</code> will consist of lowercase English&nbsp;letters (<code>&#39;a&#39;</code> to <code>&#39;z&#39;</code>) only.</li>
</ul>

<p>&nbsp;</p>


 **difficulty**: Medium

 **topic**: Greedy, Two Pointers, 

