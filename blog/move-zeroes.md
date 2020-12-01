Leetcode 283. 移动零
<p>给定一个数组 <code>nums</code>，编写一个函数将所有 <code>0</code> 移动到数组的末尾，同时保持非零元素的相对顺序。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> <code>[0,1,0,3,12]</code>

<strong>输出:</strong> <code>[1,3,12,0,0]</code></pre>



<p><strong>说明</strong>:</p>



<ol>

	<li>必须在原数组上操作，不能拷贝额外的数组。</li>

	<li>尽量减少操作次数。</li>

</ol>





 **难度**: Easy



 **标签**: 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.93% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了30.41% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0   # 当前指针
        index = 0   # 用于记录插入位置
        while i < len_nums:
            if nums[i] != 0:    # 不为0 时， 将当前数与插入位置数交换
                nums[index], nums[i] = nums[i], nums[index]
                index += 1  # 插入位置后移
            i += 1 # 处理下一个数</code></pre></div>
