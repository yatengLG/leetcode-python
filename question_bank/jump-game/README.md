<h2>55. 跳跃游戏</h2><p>给定一个非负整数数组，你最初位于数组的第一个位置。</p>

<p>数组中的每个元素代表你在该位置可以跳跃的最大长度。</p>

<p>判断你是否能够到达最后一个位置。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> [2,3,1,1,4]
<strong>输出:</strong> true
<strong>解释:</strong> 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [3,2,1,0,4]
<strong>输出:</strong> false
<strong>解释:</strong> 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
</pre>


 **难度**: Medium

 **标签**: 贪心算法、 数组、 


------

<h2>55. Jump Game</h2><p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Determine if you are able to reach the last index.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10^4</code></li>
	<li><code>0 &lt;= nums[i][j] &lt;= 10^5</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Greedy, Array, 

