<h2>968. 监控二叉树</h2><p>给定一个二叉树，我们在树的节点上安装摄像头。</p>

<p>节点上的每个摄影头都可以监视<strong>其父对象、自身及其直接子对象。</strong></p>

<p>计算监控树的所有节点所需的最小摄像头数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_01.png" style="height: 163px; width: 138px;"></p>

<pre><strong>输入：</strong>[0,0,null,0,0]
<strong>输出：</strong>1
<strong>解释：</strong>如图所示，一台摄像头足以监控所有节点。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_02.png" style="height: 312px; width: 139px;"></p>

<pre><strong>输入：</strong>[0,0,null,0,null,0,null,null,0]
<strong>输出：</strong>2
<strong>解释：</strong>需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
</pre>

<p><br>
<strong>提示：</strong></p>

<ol>
	<li>给定树的节点数的范围是&nbsp;<code>[1, 1000]</code>。</li>
	<li>每个节点的值都是 0。</li>
</ol>


 **难度**: Hard

 **标签**: 树、 深度优先搜索、 动态规划、 


------

<h2>968. Binary Tree Cameras</h2><p>Given a binary tree, we install cameras on the nodes of the tree.&nbsp;</p>

<p>Each camera at&nbsp;a node can monitor <strong>its parent, itself, and its immediate children</strong>.</p>

<p>Calculate the minimum number of cameras needed to monitor all nodes of the tree.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_01.png" style="width: 138px; height: 163px;" />
<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,0,null,0,0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>One camera is enough to monitor all nodes if placed as shown.
</pre>

<div>
<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/29/bst_cameras_02.png" style="width: 139px; height: 312px;" />
<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,0,null,0,null,0,null,null,0]</span>
<strong>Output: </strong><span id="example-output-2">2
<strong>Explanation:</strong> At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.</span>
</pre>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the given tree will be in the range&nbsp;<code>[1, 1000]</code>.</li>
	<li><strong>Every</strong> node has value 0.</li>
</ol>
</div>
</div>


 **difficulty**: Hard

 **topic**: Tree, Depth-first Search, Dynamic Programming, 

