Leetcode 34. 在排序数组中查找元素的第一个和最后一个位置
<p>给定一个按照升序排列的整数数组 <code>nums</code>，和一个目标值 <code>target</code>。找出给定目标值在数组中的开始位置和结束位置。</p>


<p>如果数组中不存在目标值 <code>target</code>，返回 <code>[-1, -1]</code>。</p>



<p><strong>进阶：</strong></p>



<ul>

	<li>你可以设计并实现时间复杂度为 <code>O(log n)</code> 的算法解决此问题吗？</li>

</ul>



<p> </p>



<p><strong>示例 1：</strong></p>



<pre>

<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 8

<strong>输出：</strong>[3,4]</pre>



<p><strong>示例 2：</strong></p>



<pre>

<strong>输入：</strong>nums = [<code>5,7,7,8,8,10]</code>, target = 6

<strong>输出：</strong>[-1,-1]</pre>



<p><strong>示例 3：</strong></p>



<pre>

<strong>输入：</strong>nums = [], target = 0

<strong>输出：</strong>[-1,-1]</pre>



<p> </p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>0 <= nums.length <= 10<sup>5</sup></code></li>

	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>

	<li><code>nums</code> 是一个非递减数组</li>

	<li><code>-10<sup>9</sup> <= target <= 10<sup>9</sup></code></li>

</ul>





 **难度**: Medium



 **标签**: 数组、 二分查找、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了74.31% 的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了12.21% 的用户

解题思路：
    二分查找，寻找target在nums中的位置
    以找到的target值，向两侧扩张
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找，寻找target
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                break
            elif nums[m] <= target:
                l = m + 1
            else:
                r = m - 1
        # 从找到的值，向两侧寻找
        if l <= r and nums[(l + r) // 2] == target:
            l, r = (l + r) // 2, (l + r) // 2
            while l-1 >= 0 and nums[l-1] == target:
                l -= 1
            while r+1 <= len(nums)-1 and nums[r+1] == target:
                r += 1
            return [l,r]
        else:
            return [-1, -1]
</code></pre></div>
