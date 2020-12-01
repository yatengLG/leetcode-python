Leetcode 47. 全排列 II
<p>给定一个可包含重复数字的序列，返回所有不重复的全排列。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> [1,1,2]

<strong>输出:</strong>

[

  [1,1,2],

  [1,2,1],

  [2,1,1]

]</pre>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了43.34% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了17.94% 的用户

解题思路：
    回溯
    由于题中存在重复元素，需要对重复元素进行跳过

"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 存在重复的，先进行排序，后续便于去重
        n = len(nums)
        result = []

        def backtrack(current:list, used:list):
            print(current)
            if len(current) >= n:
                result.append(current[:])
                return
            for i in range(n):
                if i > 0 and i-1 not in used and nums[i]==nums[i-1]:    # 去重，去重时，需要判断前一个数字是否已被使用
                    continue
                if i not in used:
                    current.append(nums[i])
                    used.append(i)
                    backtrack(current, used)
                    current.pop()
                    used.pop()

        backtrack([], [])

        return result</code></pre></div>
