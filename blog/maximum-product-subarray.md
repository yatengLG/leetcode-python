Leetcode 152. 乘积最大子数组
<p>给你一个整数数组 <code>nums</code>&nbsp;，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。</p>


<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [2,3,-2,4]

<strong>输出:</strong> <code>6</code>

<strong>解释:</strong>&nbsp;子数组 [2,3] 有最大乘积 6。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [-2,0,-1]

<strong>输出:</strong> 0

<strong>解释:</strong>&nbsp;结果不能为 2, 因为 [-2,-1] 不是子数组。</pre>





 **难度**: Medium



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了68.90% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了9.44% 的用户

解题思路：
    求子区间最大乘积，最大乘积只与 前一个相关
    但由于存在正负，所以在判断时，也记录最小值。
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_min = [[]for _ in range(n)]
        dp_max = [[]for _ in range(n)]

        dp_min[0] = nums[0]
        dp_max[0] = nums[0]

        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])

        return max(dp_max)

"""
执行用时：44 ms, 在所有 Python3 提交中击败了93.58% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了51.68% 的用户

解题思路：
    优化了一下
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre_min = nums[0]
        pre_max = nums[0]
        max_ = pre_max
        for i in range(1, n):
            p_max = max(pre_max*nums[i], pre_min*nums[i], nums[i])
            p_min = min(pre_max*nums[i], pre_min*nums[i], nums[i])
            pre_max, pre_min = p_max, p_min
            max_ = max(max_, pre_max)
        return max_
</code></pre></div>
