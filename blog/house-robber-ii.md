Leetcode 213. 打家劫舍 II
<p>你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都<strong>围成一圈，</strong>这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong>。</p>


<p>给定一个代表每个房屋存放金额的非负整数数组，计算你<strong>在不触动警报装置的情况下，</strong>能够偷窃到的最高金额。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> [2,3,2]

<strong>输出:</strong> 3

<strong>解释:</strong> 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [1,2,3,1]

<strong>输出:</strong> 4

<strong>解释:</strong> 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。

&nbsp;    偷窃到的最高金额 = 1 + 3 = 4 。</pre>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.16% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了52.73%

解题思路：
    由于头尾相连，将环拆开，[1:]与[:-1] 单独处理，并取最大值
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def f(nums):
            pre, cur = 0, 0
            for num in nums:
                cur, pre = max(pre+num, cur), cur
            return cur
        return max(f(nums[1:]), f(nums[:-1]))</code></pre></div>
