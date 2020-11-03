<h2>1282. 用户分组</h2><p>有&nbsp;<code>n</code>&nbsp;位用户参加活动，他们的&nbsp;<strong>ID</strong>&nbsp;从 <code>0</code> 到 <code>n - 1</code>，每位用户都 <strong>恰好</strong> 属于某一用户组。给你一个长度为 <code>n</code> 的数组&nbsp;<code>groupSizes</code>，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。</p>

<p>你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>groupSizes = [3,3,3,3,3,1,3]
<strong>输出：</strong>[[5],[0,1,2],[3,4,6]]
<strong>解释：</strong> 
其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>groupSizes = [2,1,3,3,3,2]
<strong>输出：</strong>[[1],[0,5],[2,3,4]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>groupSizes.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 500</code></li>
	<li><code>1 &lt;=&nbsp;groupSizes[i] &lt;= n</code></li>
</ul>


 **难度**: Medium

 **标签**: 贪心算法、 


------

<h2>1282. Group the People Given the Group Size They Belong To</h2><p>There are <code>n</code> people&nbsp;that are split into some unknown number of groups. Each person is labeled with a&nbsp;<strong>unique ID</strong>&nbsp;from&nbsp;<code>0</code>&nbsp;to&nbsp;<code>n - 1</code>.</p>

<p>You are given an integer array&nbsp;<code>groupSizes</code>, where <code>groupSizes[i]</code>&nbsp;is the size of the group that person&nbsp;<code>i</code>&nbsp;is in. For example, if&nbsp;<code>groupSizes[1] = 3</code>, then&nbsp;person&nbsp;<code>1</code>&nbsp;must be in a&nbsp;group of size&nbsp;<code>3</code>.</p>

<p>Return&nbsp;<em>a list of groups&nbsp;such that&nbsp;each person&nbsp;<code>i</code>&nbsp;is in a group of size&nbsp;<code>groupSizes[i]</code></em>.</p>

<p>Each person should&nbsp;appear in&nbsp;<strong>exactly one group</strong>,&nbsp;and every person must be in a group. If there are&nbsp;multiple answers, <strong>return any of them</strong>. It is <strong>guaranteed</strong> that there will be <strong>at least one</strong> valid solution for the given input.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> groupSizes = [3,3,3,3,3,1,3]
<strong>Output:</strong> [[5],[0,1,2],[3,4,6]]
<b>Explanation:</b> 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> groupSizes = [2,1,3,3,3,2]
<strong>Output:</strong> [[1],[0,5],[2,3,4]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>groupSizes.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 500</code></li>
	<li><code>1 &lt;=&nbsp;groupSizes[i] &lt;= n</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Greedy, 

