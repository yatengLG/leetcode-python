Leetcode 941. 有效的山脉数组
<p>给定一个整数数组&nbsp;<code>A</code>，如果它是有效的山脉数组就返回&nbsp;<code>true</code>，否则返回 <code>false</code>。</p>


<p>让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：</p>



<ul>

	<li><code>A.length &gt;= 3</code></li>

	<li>在&nbsp;<code>0 &lt; i&nbsp;&lt; A.length - 1</code>&nbsp;条件下，存在&nbsp;<code>i</code>&nbsp;使得：

	<ul>

		<li><code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] </code></li>

		<li><code>A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]</code></li>

	</ul>

	</li>

</ul>



<p>&nbsp;</p>



<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" style="height: 316px; width: 500px;"></p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[2,1]

<strong>输出：</strong>false

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[3,5,5]

<strong>输出：</strong>false

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>[0,3,2,1]

<strong>输出：</strong>true</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>0 &lt;= A.length &lt;= 10000</code></li>

	<li><code>0 &lt;= A[i] &lt;= 10000&nbsp;</code></li>

</ol>



<p>&nbsp;</p>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：236 ms, 在所有 Python3 提交中击败了93.30% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了9.53% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:  # 如果长<3，False
            return False
        if not (A[0] < A[1] and A[-1] < A[-2]): # 判断起始与结尾，如不满足则直接False
            return False

        up = True   # 记录上升状态
        for i in range(1, len(A)):
            if A[i] > A[i-1] and up:    # 如果当前上升，则跳过
                pass
            elif A[i] < A[i-1]: # 如果当前下降，则将状态至于下降
                up = False
            else:   # 如果下降状态，但数值增大，或数值不变，则False
                return False
        return True
</code></pre></div>
