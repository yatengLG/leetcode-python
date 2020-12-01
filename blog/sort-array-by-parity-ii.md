Leetcode 922. 按奇偶排序数组 II
<p>给定一个非负整数数组&nbsp;<code>A</code>， A 中一半整数是奇数，一半整数是偶数。</p>


<p>对数组进行排序，以便当&nbsp;<code>A[i]</code> 为奇数时，<code>i</code>&nbsp;也是奇数；当&nbsp;<code>A[i]</code>&nbsp;为偶数时， <code>i</code> 也是偶数。</p>



<p>你可以返回任何满足上述条件的数组作为答案。</p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>[4,2,5,7]

<strong>输出：</strong>[4,5,2,7]

<strong>解释：</strong>[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>2 &lt;= A.length &lt;= 20000</code></li>

	<li><code>A.length % 2 == 0</code></li>

	<li><code>0 &lt;= A[i] &lt;= 1000</code></li>

</ol>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 排序、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：244 ms, 在所有 Python3 提交中击败了79.21% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了21.67% 的用户

解题思路：
    单次遍历
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        num = 0
        i = 0
        while i < len(A):
            if A[i] % 2 == i % 2:   # 如果当前奇偶排序对应，则下一个元素
                i += 1
            else:
                while i+num < len(A) and A[i+num] % 2 != i % 2: # 找下一个满足奇偶排序的元素，并用num记录下标
                    num += 1
                A[i], A[i+num] = A[i+num], A[i] # 交换满足奇偶排序的项
                num -= 1    # 记录下标减1
                i += 1 # 处理下一个元素
        return A

"""
执行用时：232 ms, 在所有 Python3 提交中击败了91.19% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了13.33% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:    # 处理奇数下标
                while A[j] % 2: # 找偶数下标j对应的偶数
                    j += 2
                A[i], A[j] = A[j], A[i] # 交换i,j对应元素
        return A</code></pre></div>
