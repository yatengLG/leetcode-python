<h2>746. 使用最小花费爬楼梯</h2><p>数组的每个索引作为一个阶梯，第&nbsp;<code>i</code>个阶梯对应着一个非负数的体力花费值&nbsp;<code>cost[i]</code>(索引从0开始)。</p>

<p>每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。</p>

<p>您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> cost = [10, 15, 20]
<strong>输出:</strong> 15
<strong>解释:</strong> 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre><strong>输入:</strong> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<strong>输出:</strong> 6
<strong>解释:</strong> 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>cost</code>&nbsp;的长度将会在&nbsp;<code>[2, 1000]</code>。</li>
	<li>每一个&nbsp;<code>cost[i]</code> 将会是一个Integer类型，范围为&nbsp;<code>[0, 999]</code>。</li>
</ol>


 **难度**: Easy

 **标签**: 数组、 动态规划、 


------

<h2>746. Min Cost Climbing Stairs</h2><p>
On a staircase, the <code>i</code>-th step has some non-negative cost <code>cost[i]</code> assigned (0 indexed).
</p><p>
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> cost = [10, 15, 20]
<b>Output:</b> 15
<b>Explanation:</b> Cheapest is start on cost[1], pay that cost and go to the top.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<b>Output:</b> 6
<b>Explanation:</b> Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>cost</code> will have a length in the range <code>[2, 1000]</code>.</li>
<li>Every <code>cost[i]</code> will be an integer in the range <code>[0, 999]</code>.</li>
</ol>
</p>

 **difficulty**: Easy

 **topic**: Array, Dynamic Programming, 

