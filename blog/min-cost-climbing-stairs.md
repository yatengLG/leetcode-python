Leetcode 746. 使用最小花费爬楼梯
<p>数组的每个索引作为一个阶梯，第&nbsp;<code>i</code>个阶梯对应着一个非负数的体力花费值&nbsp;<code>cost[i]</code>(索引从0开始)。</p>


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





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了91.41% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了82.66% 的用户

解题思路：
    动态规划
    初始点可以是第一个或者第二个，单独处理这种情况
    对于大于三的点，其可以由第二个+1，也可以由第一个+2，取最小值即可
    dp[i] = min(dp[i-1], dp[i-2])

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:      # 对于单个元素，直接返回
            return cost[0]
        if n == 2:      # 两个元素，可经第一个，直接到顶；也可经第二个直接到顶
            return min(cost[0],cost[1])

        dp = [[] for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i] # 大于三的元素，依赖于前一个和前两个元素的值，最后加上本身的值
        cost = min(dp[-1], dp[-2])  # 最后需要处理，可经倒数第一个元素到顶，也可经倒数第二个元素到顶

        return cost
</code></pre></div>
