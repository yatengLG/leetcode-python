Leetcode 216. 组合总和 III
<p>找出所有相加之和为&nbsp;<em><strong>n</strong> </em>的&nbsp;<strong><em>k&nbsp;</em></strong>个数的组合<strong><em>。</em></strong>组合中只允许含有 1 -&nbsp;9 的正整数，并且每种组合中不存在重复的数字。</p>


<p><strong>说明：</strong></p>



<ul>

	<li>所有数字都是正整数。</li>

	<li>解集不能包含重复的组合。&nbsp;</li>

</ul>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 7

<strong>输出:</strong> [[1,2,4]]

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> <em><strong>k</strong></em> = 3, <em><strong>n</strong></em> = 9

<strong>输出:</strong> [[1,2,6], [1,3,5], [2,3,4]]

</pre>





 **难度**: Medium



 **标签**: 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.19% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.93% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))   # 1~9
        result = []

        def backtrack(begin, current:list):

            if sum(current) == n and len(current) == k: # 如果和等于n, 且个数等于k， 则添加到最终结果中
                result.append(current[:])
                return

            if sum(current) > n or len(current) > k:    # 如果和大于9 或 当前列表长度大于k， 则跳出
                return

            for i in range(begin, 9):
                current.append(nums[i])
                backtrack(i+1, current) # 查看下一个
                current.pop()   # 回溯

        backtrack(0, [])
        return result</code></pre></div>
