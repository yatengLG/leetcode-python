<h2>993. 二叉树的堂兄弟节点</h2><p>在二叉树中，根节点位于深度 <code>0</code> 处，每个深度为 <code>k</code> 的节点的子节点位于深度 <code>k+1</code> 处。</p>

<p>如果二叉树的两个节点深度相同，但<strong>父节点不同</strong>，则它们是一对<em>堂兄弟节点</em>。</p>

<p>我们给出了具有唯一值的二叉树的根节点 <code>root</code>，以及树中两个不同节点的值 <code>x</code> 和 <code>y</code>。</p>

<p>只有与值 <code>x</code> 和 <code>y</code> 对应的节点是堂兄弟节点时，才返回 <code>true</code>。否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：<br>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png" style="height: 160px; width: 180px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3,4], x = 4, y = 3
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：<br>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png" style="height: 160px; width: 201px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3,null,4,null,5], x = 5, y = 4
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png" style="height: 160px; width: 156px;"></strong></p>

<pre><strong>输入：</strong>root = [1,2,3,null,4], x = 2, y = 3
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>二叉树的节点数介于&nbsp;<code>2</code> 到&nbsp;<code>100</code>&nbsp;之间。</li>
	<li>每个节点的值都是唯一的、范围为&nbsp;<code>1</code> 到&nbsp;<code>100</code>&nbsp;的整数。</li>
</ol>

<p>&nbsp;</p>


 **难度**: Easy

 **标签**: 树、 广度优先搜索、 


------

<h2>993. Cousins in Binary Tree</h2><p>In a binary tree, the root node is at depth <code>0</code>, and children of each depth <code>k</code> node are at depth <code>k+1</code>.</p>

<p>Two nodes of a binary tree are <em>cousins</em> if they have the same depth, but have <strong>different parents</strong>.</p>

<p>We are given the <code>root</code> of a binary tree with unique values, and the values <code>x</code>&nbsp;and <code>y</code>&nbsp;of two different nodes in the tree.</p>

<p>Return&nbsp;<code>true</code>&nbsp;if and only if the nodes corresponding to the values <code>x</code> and <code>y</code> are cousins.</p>

<p>&nbsp;</p>

<p><strong>Example 1:<br />
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png" style="width: 180px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[1,2,3,4]</span>, x = <span id="example-input-1-2">4</span>, y = <span id="example-input-1-3">3</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:<br />
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png" style="width: 201px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[1,2,3,null,4,null,5]</span>, x = <span id="example-input-2-2">5</span>, y = <span id="example-input-2-3">4</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png" style="width: 156px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[1,2,3,null,4]</span>, x = 2, y = 3
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be between <code>2</code> and <code>100</code>.</li>
	<li>Each node has a unique integer value from <code>1</code> to <code>100</code>.</li>
</ul>


 **difficulty**: Easy

 **topic**: Tree, Breadth-first Search, 

