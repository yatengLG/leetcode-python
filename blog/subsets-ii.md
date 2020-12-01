Leetcode 90. 子集 II
<p>给定一个可能包含重复元素的整数数组 <em><strong>nums</strong></em>，返回该数组所有可能的子集（幂集）。</p>


<p><strong>说明：</strong>解集不能包含重复的子集。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [1,2,2]

<strong>输出:</strong>

[

  [2],

  [1],

  [1,2,2],

  [2,2],

  [1,2],

  []

]</pre>





 **难度**: Medium



 **标签**: 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了98.41% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了28.77% 的用户

解题思路：
    回溯
    先排序，指定起始元素下标，跳过重复元素
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     # 先排序，便于处理重复元素
        n = len(nums)
        result = []
        def backtrack(i, current):  # 从第i个元素作为起始
            result.append(current[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:    # 如果遇到重复的元素则跳过
                    continue
                current.append(nums[j])
                backtrack(j + 1, current)   # 下一个元素
                current.pop()   # 回溯
        backtrack(0, [])
        return result</code></pre></div>
