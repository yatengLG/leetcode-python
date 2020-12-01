Leetcode 53. 最大子序和
<p>给定一个整数数组 <code>nums</code>&nbsp;，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [-2,1,-3,4,-1,2,1,-5,4]

<strong>输出:</strong> 6

<strong>解释:</strong>&nbsp;连续子数组&nbsp;[4,-1,2,1] 的和最大，为&nbsp;6。

</pre>



<p><strong>进阶:</strong></p>



<p>如果你已经实现复杂度为 O(<em>n</em>) 的解法，尝试使用更为精妙的分治法求解。</p>





 **难度**: Easy



 **标签**: 数组、 分治算法、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了77.21% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了43.31% 的用户

解题思路：
    动态规划
    从第一个元素开始
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
         i
    dp[i] = max(dp[i-1]+num[i], num[i])

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[] for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)</code></pre></div>
