<h2>817. 链表组件</h2><p>给定链表头结点&nbsp;<code>head</code>，该链表上的每个结点都有一个 <strong>唯一的整型值</strong> 。</p>

<p>同时给定列表&nbsp;<code>G</code>，该列表是上述链表中整型值的一个子集。</p>

<p>返回列表&nbsp;<code>G</code>&nbsp;中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表&nbsp;<code>G</code>&nbsp;中）构成的集合。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre><strong>输入:</strong> 
head: 0-&gt;1-&gt;2-&gt;3
G = [0, 1, 3]
<strong>输出:</strong> 2
<strong>解释:</strong> 
链表中,0 和 1 是相连接的，且 G 中不包含 2，所以 [0, 1] 是 G 的一个组件，同理 [3] 也是一个组件，故返回 2。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> 
head: 0-&gt;1-&gt;2-&gt;3-&gt;4
G = [0, 3, 1, 4]
<strong>输出:</strong> 2
<strong>解释:</strong> 
链表中，0 和 1 是相连接的，3 和 4 是相连接的，所以 [0, 1] 和 [3, 4] 是两个组件，故返回 2。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>如果&nbsp;<code>N</code>&nbsp;是给定链表&nbsp;<code>head</code>&nbsp;的长度，<code>1 &lt;= N &lt;= 10000</code>。</li>
	<li>链表中每个结点的值所在范围为&nbsp;<code>[0, N - 1]</code>。</li>
	<li><code>1 &lt;= G.length &lt;= 10000</code></li>
	<li><code>G</code> 是链表中所有结点的值的一个子集.</li>
</ul>


 **难度**: Medium

 **标签**: 链表、 


------

<h2>817. Linked List Components</h2><p>We are given&nbsp;<code>head</code>,&nbsp;the head node of a linked list containing&nbsp;<strong>unique integer values</strong>.</p>

<p>We are also given the list&nbsp;<code>G</code>, a subset of the values in the linked list.</p>

<p>Return the number of connected components in <code>G</code>, where two values are connected if they appear consecutively in the linked list.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3
G = [0, 1, 3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
head: 0-&gt;1-&gt;2-&gt;3-&gt;4
G = [0, 3, 1, 4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li>If&nbsp;<code>N</code>&nbsp;is the&nbsp;length of the linked list given by&nbsp;<code>head</code>,&nbsp;<code>1 &lt;= N &lt;= 10000</code>.</li>
	<li>The value of each node in the linked list will be in the range<code> [0, N - 1]</code>.</li>
	<li><code>1 &lt;= G.length &lt;= 10000</code>.</li>
	<li><code>G</code> is a subset of all values in the linked list.</li>
</ul>


 **difficulty**: Medium

 **topic**: Linked List, 

