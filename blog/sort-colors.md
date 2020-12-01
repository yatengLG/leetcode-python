Leetcode 75. 颜色分类
<p>给定一个包含红色、白色和蓝色，一共&nbsp;<em>n </em>个元素的数组，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>


<p>此题中，我们使用整数 0、&nbsp;1 和 2 分别表示红色、白色和蓝色。</p>



<p><strong>注意:</strong><br>

不能使用代码库中的排序函数来解决这道题。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [2,0,2,1,1,0]

<strong>输出:</strong> [0,0,1,1,2,2]</pre>



<p><strong>进阶：</strong></p>



<ul>

	<li>一个直观的解决方案是使用计数排序的两趟扫描算法。<br>

	首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。</li>

	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>

</ul>





 **难度**: Medium



 **标签**: 排序、 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.58% 的用户
内存消耗：13.1 MB, 在所有 Python3 提交中击败了97.34% 的用户

解题思路：
    指针。将蓝色放到末尾，将红色放到起始。
    为避免无限循环，使用一个指针标记蓝色的放置位置
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = 0   # 指针，指向当前处理元素
        r = n-1 # 用于指向蓝色的放置位置。
        while index < r+1:
            # print(nums, index)
            if nums[index] == 0:
                nums.insert(0, nums.pop(index)) # 取出0，放到列表头部，index后移
                index += 1  # 指针+1
            elif nums[index] == 2:
                nums.insert(r, nums.pop(index)) # 取出2， 放到r指针指向位置，r前移。index不动
                r -= 1
            else:   # 1不处理， index后移
                index += 1</code></pre></div>
