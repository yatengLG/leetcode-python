Leetcode 剑指 Offer 42. 连续子数组的最大和
<p>输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。</p>


<p>要求时间复杂度为O(n)。</p>



<p>&nbsp;</p>



<p><strong>示例1:</strong></p>



<pre><strong>输入:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]

<strong>输出:</strong> 6

<strong>解释:</strong>&nbsp;连续子数组&nbsp;[4,-1,2,1] 的和最大，为&nbsp;6。</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;=&nbsp;arr.length &lt;= 10^5</code></li>

	<li><code>-100 &lt;= arr[i] &lt;= 100</code></li>

</ul>



<p>注意：本题与主站 53 题相同：<a href="https://leetcode-cn.com/problems/maximum-subarray/">https://leetcode-cn.com/problems/maximum-subarray/</a></p>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 分治算法、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了46.93% 的用户
内存消耗：23.3 MB, 在所有 Python3 提交中击败了5.02% 的用户
解题思路：
    动态规划
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[] for _ in range(n)]

        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)


"""
执行用时：72 ms, 在所有 Python3 提交中击败了86.48% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了70.63% 的用户

解题思路：
    同动态规划，但不采用记录的方式，而是更新最大和.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        max_ = nums[0]
        record = nums[0]
        for i in range(1, n):
            record = max(record+nums[i], nums[i])
            if record > max_:
                max_ = record
        return max_</code></pre></div>
