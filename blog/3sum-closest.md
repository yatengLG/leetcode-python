Leetcode 16. 最接近的三数之和
<p>给定一个包括&nbsp;<em>n</em> 个整数的数组&nbsp;<code>nums</code><em>&nbsp;</em>和 一个目标值&nbsp;<code>target</code>。找出&nbsp;<code>nums</code><em>&nbsp;</em>中的三个整数，使得它们的和与&nbsp;<code>target</code>&nbsp;最接近。返回这三个数的和。假定每组输入只存在唯一答案。</p>


<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>nums = [-1,2,1,-4], target = 1

<strong>输出：</strong>2

<strong>解释：</strong>与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>3 &lt;= nums.length &lt;= 10^3</code></li>

	<li><code>-10^3&nbsp;&lt;= nums[i]&nbsp;&lt;= 10^3</code></li>

	<li><code>-10^4&nbsp;&lt;= target&nbsp;&lt;= 10^4</code></li>

</ul>





 **难度**: Medium



 **标签**: 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：132 ms, 在所有 Python3 提交中击败了51.24% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了91.44% 的用户

解题思路：
    双指针法
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        n = len(nums)
        now = None
        for i in range(n):
            if nums[i] == now:  # 遇到重复的值，跳过
                continue
            now = nums[i]

            l, r = i+1, n-1 # 左右指针
            while l < r:  # 左指针小于右指针，循环
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ == target:    # 和为0
                    return target
                if abs(target - sum_) < abs(target - result):
                    result = sum_
                elif sum_ < target:     # 和 < target， 左指针右移
                    l += 1
                else:   # 和 > target， 右指针左移
                    r -= 1
        return result

"""
执行用时：48 ms, 在所有 Python3 提交中击败了98.70% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了50.46% 的用户

解题思路：
    
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        n = len(nums)
        now = None
        for i in range(n-2):
            if nums[i] == now:
                continue
            now = nums[i]

            l, r = i+1, n-1
            if nums[i]+nums[r-1]+nums[r] <= target:     # 判断当前值与最大的俩个值的和    ### 优化
                l = r-1
            elif nums[i]+nums[l]+nums[l+1] >= target:   # 判断当前值与最小的俩个值的和    ### 优化
                r = l+1
            while l < r:
                sum_ = nums[i]+nums[l]+nums[r]

                if sum_ == target:    # 和为0
                    return target
                if abs(target - sum_) < abs(target - result):
                    result = sum_
                elif sum_ < target:     # 和 < target， 左指针右移
                    l += 1
                else:   # 和 > target， 右指针左移
                    r -= 1
        return result
</code></pre></div>
