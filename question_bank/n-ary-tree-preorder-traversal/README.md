<h2>589. N叉树的前序遍历</h2><p>给定一个 N 叉树，返回其节点值的<em>前序遍历</em>。</p>

<p>例如，给定一个&nbsp;<code>3叉树</code>&nbsp;:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;"></p>

<p>&nbsp;</p>

<p>返回其前序遍历: <code>[1,3,5,6,2,4]</code>。</p>

<p>&nbsp;</p>

<p><strong>说明:&nbsp;</strong>递归法很简单，你可以使用迭代法完成此题吗?</p>

 **难度**: Easy

 **标签**: 树、 


------

<h2>589. N-ary Tree Preorder Traversal</h2><p>Given an n-ary tree, return the <i>preorder</i> traversal of its nodes&#39; values.</p>

<p><em>Nary-Tree input serialization&nbsp;is represented in their level order traversal, each group of children is separated by the null value (See examples).</em></p>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<p>Recursive solution is trivial, could you do it iteratively?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,5,6]
<strong>Output:</strong> [1,3,5,6,2,4]
</pre>

<p><strong>Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;" /></p>

<pre>
<strong>Input:</strong> root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
<strong>Output:</strong> [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The height of the n-ary tree is less than or equal to <code>1000</code></li>
	<li>The total number of nodes is between <code>[0,&nbsp;10^4]</code></li>
</ul>


 **difficulty**: Easy

 **topic**: Tree, 

