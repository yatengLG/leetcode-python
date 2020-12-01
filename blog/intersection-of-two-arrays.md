Leetcode 349. 两个数组的交集
<p>给定两个数组，编写一个函数来计算它们的交集。</p>


<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>nums1 = [1,2,2,1], nums2 = [2,2]

<strong>输出：</strong>[2]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>nums1 = [4,9,5], nums2 = [9,4,9,8,4]

<strong>输出：</strong>[9,4]</pre>



<p>&nbsp;</p>



<p><strong>说明：</strong></p>



<ul>

	<li>输出结果中的每个元素一定是唯一的。</li>

	<li>我们可以不考虑输出结果的顺序。</li>

</ul>





 **难度**: Easy



 **标签**: 排序、 哈希表、 双指针、 二分查找、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了85.56% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.23% 的用户

解题思路：
    集合 去重
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        return [i for i in nums1 if i in nums2]</code></pre></div>
