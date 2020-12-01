Leetcode 338. 比特位计数
<p>给定一个非负整数&nbsp;<strong>num</strong>。对于&nbsp;<strong>0 &le; i &le; num </strong>范围中的每个数字&nbsp;<strong>i&nbsp;</strong>，计算其二进制数中的 1 的数目并将它们作为数组返回。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入: </strong>2

<strong>输出: </strong>[0,1,1]</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入: </strong>5

<strong>输出: </strong><code>[0,1,1,2,1,2]</code></pre>



<p><strong>进阶:</strong></p>



<ul>

	<li>给出时间复杂度为<strong>O(n*sizeof(integer))</strong>的解答非常容易。但你可以在线性时间<strong>O(n)</strong>内用一趟扫描做到吗？</li>

	<li>要求算法的空间复杂度为<strong>O(n)</strong>。</li>

	<li>你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的&nbsp;<strong>__builtin_popcount</strong>）来执行此操作。</li>

</ul>





 **难度**: Medium



 **标签**: 位运算、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了92.93% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了23.45% 的用户

解题思路：
    某一数值num的比特位为1的计数，等于其 /2的余数为1 的数量
    例：
            13  余                  6   余
        /2  6   1               /2  3   0
        /2  3   0               /2  1   1
        /2  1   1               /2  0   1
        /2  0   1

"""
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            dp[i] = dp[i // 2] if i%2 == 0 else dp[i // 2]+1
        return dp</code></pre></div>
