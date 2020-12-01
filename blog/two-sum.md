Leetcode 1. 两数之和
<p>给定一个整数数组 <code>nums</code>&nbsp;和一个目标值 <code>target</code>，请你在该数组中找出和为目标值的那&nbsp;<strong>两个</strong>&nbsp;整数，并返回他们的数组下标。</p>


<p>你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre>给定 nums = [2, 7, 11, 15], target = 9



因为 nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9

所以返回 [<strong>0, 1</strong>]

</pre>





 **难度**: Easy



 **标签**: 数组、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了96.65% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.48% 的用户

解题思路：
    使用字典存储，快速查找
"""
class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        record = {}
        for i, v in enumerate(nums):
            a = target-v
            if a not in record:
                record[v] = i
            else:
                return [i, record[a]]
</code></pre></div>
