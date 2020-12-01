Leetcode 39. 组合总和
<p>给定一个<strong>无重复元素</strong>的数组&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>


<p><code>candidates</code>&nbsp;中的数字可以无限制重复被选取。</p>



<p><strong>说明：</strong></p>



<ul>

	<li>所有数字（包括&nbsp;<code>target</code>）都是正整数。</li>

	<li>解集不能包含重复的组合。&nbsp;</li>

</ul>



<p><strong>示例&nbsp;1：</strong></p>



<pre><strong>输入：</strong>candidates = <code>[2,3,6,7], </code>target = <code>7</code>,

<strong>所求解集为：</strong>

[

  [7],

  [2,2,3]

]

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入：</strong>candidates = [2,3,5]<code>, </code>target = 8,

<strong>所求解集为：</strong>

[

&nbsp; [2,2,2,2],

&nbsp; [2,3,3],

&nbsp; [3,5]

]</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>

	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>

	<li><code>candidate</code> 中的每个元素都是独一无二的。</li>

	<li><code>1 &lt;= target &lt;= 500</code></li>

</ul>





 **难度**: Medium



 **标签**: 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了91.06% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了42.14% 的用户

解题思路：
    递归
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)
        def backtrack(index, target, current):  # 递归，开始的下标，目标值，当前数组
            for i in range(index, n):
                num = candidates[i]
                if num == target:
                    result.append(current+[num])    # 当前数组下 某值与目标值相等，则加入到结果中
                elif num > target:  # 数值大于目标值，则跳出
                    return
                else:               # 小于目标值，下一层
                    backtrack(i, target-num, current+[num])
        backtrack(0, target, [])
        return result</code></pre></div>
