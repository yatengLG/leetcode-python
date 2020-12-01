Leetcode 996. 正方形数组的数目
<p>给定一个非负整数数组&nbsp;<code>A</code>，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为<em>正方形</em>数组。</p>


<p>返回 A 的正方形排列的数目。两个排列 <code>A1</code> 和 <code>A2</code> 不同的充要条件是存在某个索引 <code>i</code>，使得 A1[i] != A2[i]。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[1,17,8]

<strong>输出：</strong>2

<strong>解释：</strong>

[1,8,17] 和 [17,8,1] 都是有效的排列。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[2,2,2]

<strong>输出：</strong>1

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= A.length &lt;= 12</code></li>

	<li><code>0 &lt;= A[i] &lt;= 1e9</code></li>

</ol>





 **难度**: Hard



 **标签**: 图、 数学、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了73.57% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了70.71% 的用户

解题思路：
    回溯+剪枝
"""
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        result = []
        n = len(A)
        A.sort()    # 排序，便于重复元素剪枝
        def backtrack(index, current, used):    # 当前节点索引， 当前列表， 使用用的索引
            if len(current) == n and current not in result: # 如果当前列表包含了所有A元素，添加到最终结果中
                result.append(current)
                return

            for i in range(n):
                if i not in used:   # 循环A，对于没有使用过的元素
                    num = (A[index] + A[i]) ** 0.5  # 计算开方
                    if i > 0 and A[i] == A[i-1] and i-1 not in used:    # 重复元素剪枝
                        continue
                    if int(num) == num: # 如果是完全平方数，则将A[i]添加到当前列表
                        backtrack(i, current+[A[i]], used+[i])  # 把index更新为i

        for index in range(n):  # 已不同下标开始
            if index > 0 and A[index] == A[index-1]:    # 跳过相同元素
                continue
            backtrack(index, [A[index]], [index])

        return len(result)</code></pre></div>
