<h2>109. 有序链表转换二叉搜索树</h2><p>给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。</p>

<p>本题中，一个高度平衡二叉树是指一个二叉树<em>每个节点&nbsp;</em>的左右两个子树的高度差的绝对值不超过 1。</p>

<p><strong>示例:</strong></p>

<pre>给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
</pre>


 **难度**: Medium

 **标签**: 深度优先搜索、 链表、 


------

<h2>109. Convert Sorted List to Binary Search Tree</h2><p>Given the <code>head</code> of a singly linked list where elements are <strong>sorted in ascending order</strong>, convert it to a height balanced BST.</p>

<p>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/linked.jpg" style="width: 600px; height: 466px;" />
<pre>
<strong>Input:</strong> head = [-10,-3,0,5,9]
<strong>Output:</strong> [0,-3,9,-10,null,5]
<strong>Explanation:</strong> One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> head = [1,3]
<strong>Output:</strong> [3,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The numner of nodes in <code>head</code> is in the range <code>[0, 2 * 10^4]</code>.</li>
	<li><code>-10^5 &lt;= Node.val &lt;= 10^5</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Depth-first Search, Linked List, 

