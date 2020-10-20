<h2>331. 验证二叉树的前序序列化</h2><p>序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 <code>#</code>。</p>

<pre>     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
</pre>

<p>例如，上面的二叉树可以被序列化为字符串 <code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>，其中 <code>#</code> 代表一个空节点。</p>

<p>给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。</p>

<p>每个以逗号分隔的字符或为一个整数或为一个表示 <code>null</code> 指针的 <code>&#39;#&#39;</code> 。</p>

<p>你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如&nbsp;<code>&quot;1,,3&quot;</code> 。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong><code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>
<strong>输出: </strong><code>true</code></pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong><code>&quot;1,#&quot;</code>
<strong>输出: </strong><code>false</code>
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入: </strong><code>&quot;9,#,#,1&quot;</code>
<strong>输出: </strong><code>false</code></pre>


 **难度**: Medium

 **标签**: 栈、 


------

<h2>331. Verify Preorder Serialization of a Binary Tree</h2><p>One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node&#39;s value. If it is a null node, we record using a sentinel value such as <code>#</code>.</p>

<pre>
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
</pre>

<p>For example, the above binary tree can be serialized to the string <code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>, where <code>#</code> represents a null node.</p>

<p>Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.</p>

<p>Each comma separated value in the string must be either an integer or a character <code>&#39;#&#39;</code> representing <code>null</code> pointer.</p>

<p>You may assume that the input format is always valid, for example it could never contain two consecutive commas such as <code>&quot;1,,3&quot;</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong><code>&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>
<strong>Output: </strong><code>true</code></pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong><code>&quot;1,#&quot;</code>
<strong>Output: </strong><code>false</code>
</pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input: </strong><code>&quot;9,#,#,1&quot;</code>
<strong>Output: </strong><code>false</code></pre>

 **difficulty**: Medium

 **topic**: Stack, 

