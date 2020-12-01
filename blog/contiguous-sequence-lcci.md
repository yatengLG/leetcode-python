Leetcode 面试题 16.17. 连续数列
<p>给定一个整数数组，找出总和最大的连续数列，并返回总和。</p>


<p><strong>示例：</strong></p>



<pre><strong>输入：</strong> [-2,1,-3,4,-1,2,1,-5,4]

<strong>输出：</strong> 6

<strong>解释：</strong> 连续子数组 [4,-1,2,1] 的和最大，为 6。

</pre>



<p><strong>进阶：</strong></p>



<p>如果你已经实现复杂度为 O(<em>n</em>) 的解法，尝试使用更为精妙的分治法求解。</p>





 **难度**: Easy



 **标签**: 数组、 分治算法、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了75.32% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.49% 的用户

解题思路：
    动态规划
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[] for _ in range(n)]

        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

"""
执行用时：40 ms, 在所有 Python3 提交中击败了96.92% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了90.98% 的用户

解题思路：
    动态规划，但是不记录每一步的值，改用比较更新的方式去寻找最大值
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        max_ = nums[0]
        for i in range(1, n):
            max_ = max(max_+nums[i], nums[i])
            if max_ > result:
                result = max_
        return result
</code></pre></div>
