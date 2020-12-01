Leetcode 35. 搜索插入位置
<p>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>


<p>你可以假设数组中无重复元素。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [1,3,5,6], 5

<strong>输出:</strong> 2

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> [1,3,5,6], 2

<strong>输出:</strong> 1

</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入:</strong> [1,3,5,6], 7

<strong>输出:</strong> 4

</pre>



<p><strong>示例 4:</strong></p>



<pre><strong>输入:</strong> [1,3,5,6], 0

<strong>输出:</strong> 0

</pre>





 **难度**: Easy



 **标签**: 数组、 二分查找、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG
"""
执行用时：32 ms, 在所有 Python3 提交中击败了97.41% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了29.36% 的用户

解题思路：
    双指针二分查找
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1   # 左右指针
        if target <= nums[l]:   # 处理小于左值情况，小于最小值，在0处插入(当等于时, 也返回0)
            return l

        if target > nums[r]:    # 大于最大值， 在r+1处插入
            return r+1

        while r-l > 1:          # 当左指针与右指针不相临时，循环
            m = l+(r-l)//2      # 中间指针
            if nums[m] == target:   # 如果等于，则返回当前指针
                return m
            elif nums[m] < target:  # 小于目标值，值处于m-r之间，更新左指针为m
                l = m
            else:
                r = m               # m指针值大于目标值，值处于l-m之间，更新右指针为m
        return r</code></pre></div>
