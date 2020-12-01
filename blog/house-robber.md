Leetcode 198. 打家劫舍
<p>你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong>。</p>


<p>给定一个代表每个房屋存放金额的非负整数数组，计算你<strong> 不触动警报装置的情况下 </strong>，一夜之内能够偷窃到的最高金额。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[1,2,3,1]

<strong>输出：</strong>4

<strong>解释：</strong>偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。

&nbsp;    偷窃到的最高金额 = 1 + 3 = 4 。</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[2,7,9,3,1]

<strong>输出：</strong>12

<strong>解释：</strong>偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。

&nbsp;    偷窃到的最高金额 = 2 + 9 + 1 = 12 。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>0 &lt;= nums.length &lt;= 100</code></li>

	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>

</ul>





 **难度**: Easy



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了87.93% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了55.99% 的用户

解题思路：
    动态规划
    由于不能挨着偷取，所以 当前偷取的值依赖于上上一个
        dp[i] == dp[i-2]+nums[i]
    当前偷取的最大值为
        dp[i] == max(dp[i-2]+nums[i], dp[i-1])
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n < 3:
            return max(nums)
        dp = [[] for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return max(dp)
</code></pre></div>
