Leetcode 169. 多数元素
<p>给定一个大小为 <em>n </em>的数组，找到其中的多数元素。多数元素是指在数组中出现次数<strong>大于</strong>&nbsp;<code>&lfloor; n/2 &rfloor;</code>&nbsp;的元素。</p>


<p>你可以假设数组是非空的，并且给定的数组总是存在多数元素。</p>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> [3,2,3]

<strong>输出:</strong> 3</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> [2,2,1,1,1,2,2]

<strong>输出:</strong> 2

</pre>





 **难度**: Easy



 **标签**: 位运算、 数组、 分治算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了90.24% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了58.08% 的用户

解题思路：
    既然是多数元素，出现次数大于n//2。
    则排序后，n//2必然是多数元素
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]</code></pre></div>
