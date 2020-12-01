Leetcode 861. 翻转矩阵后的得分
<p>有一个二维矩阵&nbsp;<code>A</code> 其中每个元素的值为&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code>&nbsp;。</p>


<p>移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 <code>0</code> 都更改为 <code>1</code>，将所有 <code>1</code> 都更改为 <code>0</code>。</p>



<p>在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。</p>



<p>返回尽可能高的分数。</p>



<p>&nbsp;</p>



<ol>

</ol>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>[[0,0,1,1],[1,0,1,0],[1,1,0,0]]

<strong>输出：</strong>39

<strong>解释：

</strong>转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]

0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= A.length &lt;= 20</code></li>

	<li><code>1 &lt;= A[0].length &lt;= 20</code></li>

	<li><code>A[i][j]</code>&nbsp;是&nbsp;<code>0</code> 或&nbsp;<code>1</code></li>

</ol>





 **难度**: Medium



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了98.48% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了6.28% 的用户

解题思路：
    现将对行进行翻转，将每行第一个变为1
    其次，对列进行变换，如果本列0数量较多，则翻转
"""
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):  # 按行，如果每行第一个为0，则翻转该行
            if A[i][0] == 0:
                A[i] = [1 if a == 0 else 0 for a in A[i]]

        for j in range(n):  # 按列
            sum_ = 0
            for i in range(m):
                sum_ += A[i][j] # 统计本行非0值
            if sum_ < m/2:  # 如果非0值少，则翻转该列
                for i in range(m):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        result = 0
        for a in A:
            result += int('0b'+''.join([str(aa) for aa in a]), base=2)
        return result</code></pre></div>
