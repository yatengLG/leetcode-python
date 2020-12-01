Leetcode 面试题 17.16. 按摩师
<p>一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。</p>


<p><strong>注意：</strong>本题相对原题稍作改动</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong> [1,2,3,1]

<strong>输出：</strong> 4

<strong>解释：</strong> 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong> [2,7,9,3,1]

<strong>输出：</strong> 12

<strong>解释：</strong> 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong> [2,1,4,5,3,1,1,3]

<strong>输出：</strong> 12

<strong>解释：</strong> 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

</pre>





 **难度**: Easy



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：16 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.92% 的用户

解题思路：
    动态规划
    由于中间需要休息，也就是最少需要间隔一个元素，所以在计算当前点时，需要跳过一个元素往前看
    但由于在计算时，必须相隔一个元素，这样就造成相领两个元素的值大小不定。
    这样在计算时，就必须，跳过前一个元素，比较之前两个元素的大小
    dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
"""

class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[:2])
        if n == 2:
            return max(nums[0]+nums[2], nums[1])

        dp = [[] for _ in range(n)]

        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        dp[2] = max(nums[0]+nums[2], nums[1])

        for i in range(3, n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]

        return max(dp[-2:])
</code></pre></div>
