Leetcode 78. 子集
<p>给定一组<strong>不含重复元素</strong>的整数数组&nbsp;<em>nums</em>，返回该数组所有可能的子集（幂集）。</p>


<p><strong>说明：</strong>解集不能包含重复的子集。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> nums = [1,2,3]

<strong>输出:</strong>

[

  [3],

&nbsp; [1],

&nbsp; [2],

&nbsp; [1,2,3],

&nbsp; [1,3],

&nbsp; [2,3],

&nbsp; [1,2],

&nbsp; []

]</pre>





 **难度**: Medium



 **标签**: 位运算、 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.34% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了63.97% 的用户

解题思路：
    回溯
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def backtrack(i, current):  # 从第i个元素开始
            # print(current)
            result.append(current[:])
            if i >= n:  # 当遍历到
                return

            for j in range(i, n):
                current.append(nums[j])
                backtrack(j + 1, current)   # 下一个
                current.pop()               # 回溯

        backtrack(0, [])
        return result</code></pre></div>
