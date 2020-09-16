<h2>897. 递增顺序查找树</h2><p>给你一个树，请你 <strong>按中序遍历</strong> 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。</p>

<p>&nbsp;</p>

<p><strong>示例 ：</strong></p>

<pre><strong>输入：</strong>[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
&nbsp;/        / \ 
1        7   9

<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
&nbsp; \
&nbsp;  2
&nbsp;   \
&nbsp;    3
&nbsp;     \
&nbsp;      4
&nbsp;       \
&nbsp;        5
&nbsp;         \
&nbsp;          6
&nbsp;           \
&nbsp;            7
&nbsp;             \
&nbsp;              8
&nbsp;               \
                 9  </pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>给定树中的结点数介于 <code>1</code> 和&nbsp;<code>100</code> 之间。</li>
	<li>每个结点都有一个从 <code>0</code> 到 <code>1000</code> 范围内的唯一整数值。</li>
</ol>


 **难度**: Easy

 **标签**: 树、 深度优先搜索、 


------

<h2>897. Increasing Order Search Tree</h2><p>Given a binary search tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
&nbsp;/        / \ 
1        7   9

<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
&nbsp; \
&nbsp;  2
&nbsp;   \
&nbsp;    3
&nbsp;     \
&nbsp;      4
&nbsp;       \
&nbsp;        5
&nbsp;         \
&nbsp;          6
&nbsp;           \
&nbsp;            7
&nbsp;             \
&nbsp;              8
&nbsp;               \
                 9  </pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be between <code>1</code> and <code>100</code>.</li>
	<li>Each node will have a unique integer value from <code>0</code> to <code>1000</code>.</li>
</ul>


 **difficulty**: Easy

 **topic**: Tree, Depth-first Search, 

