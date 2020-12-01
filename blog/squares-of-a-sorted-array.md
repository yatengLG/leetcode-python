Leetcode 977. 有序数组的平方
<p>给定一个按非递减顺序排序的整数数组 <code>A</code>，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。</p>


<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[-4,-1,0,3,10]

<strong>输出：</strong>[0,1,9,16,100]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[-7,-3,2,3,11]

<strong>输出：</strong>[4,9,9,49,121]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= A.length &lt;= 10000</code></li>

	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>

	<li><code>A</code>&nbsp;已按非递减顺序排序。</li>

</ol>





 **难度**: Easy



 **标签**: 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：296 ms, 在所有 Python3 提交中击败了45.62% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.22% 的用户

解题思路：
    先处理小于0的值，平方后直接添加到最终结果中
    然后处理>=0的值，并用一个q指针记录在result中的插入位置
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [a**2 for a in A if a<0][::-1]
        pos = [a**2 for a in A if a>=0]
        # print(pos, result)
        q = 0
        for p in pos:
            if result == [] or p > result[-1]:
                result += [p]
            else:
                while p > result[q]:
                    q = q + 1
                result.insert(q, p)
        return result

"""
执行用时：284 ms, 在所有 Python3 提交中击败了56.45% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.22% 的用户
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [a**2 for a in A]
        result.sort()
        return result
</code></pre></div>
