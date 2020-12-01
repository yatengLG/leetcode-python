Leetcode 面试题 08.04. 幂集
<p>幂集。编写一种方法，返回某集合的所有子集。集合中<strong>不包含重复的元素</strong>。</p>


<p>说明：解集不能包含重复的子集。</p>



<p><strong>示例:</strong></p>



<pre><strong> 输入</strong>： nums = [1,2,3]

<strong> 输出</strong>：

[

  [3],

&nbsp; [1],

&nbsp; [2],

&nbsp; [1,2,3],

&nbsp; [1,3],

&nbsp; [2,3],

&nbsp; [1,2],

&nbsp; []

]

</pre>





 **难度**: Medium



 **标签**: 位运算、 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了96.84% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了24.26% 的用户

解题思路：
    回溯
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 先排序，方便处理重复元素
        n = len(nums)
        result = []

        def backtrack(index, current):
            result.append(current[:])
            if index >= n:
                return
            for i in range(index, n):
                if i>0 and nums[i] == nums[i-1]:    # 跳过重复元素
                    continue
                backtrack(i+1, current+[nums[i]])
        backtrack(0, [])
        return result
</code></pre></div>
