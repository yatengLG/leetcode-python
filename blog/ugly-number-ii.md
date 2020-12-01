Leetcode 264. 丑数 II
<p>编写一个程序，找出第 <code>n</code> 个丑数。</p>


<p>丑数就是质因数只包含&nbsp;<code>2, 3, 5</code> 的<strong>正整数</strong>。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> n = 10

<strong>输出:</strong> 12

<strong>解释: </strong><code>1, 2, 3, 4, 5, 6, 8, 9, 10, 12</code> 是前 10 个丑数。</pre>



<p><strong>说明:&nbsp;</strong>&nbsp;</p>



<ol>

	<li><code>1</code>&nbsp;是丑数。</li>

	<li><code>n</code>&nbsp;<strong>不超过</strong>1690。</li>

</ol>





 **难度**: Medium



 **标签**: 堆、 数学、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：164 ms, 在所有 Python3 提交中击败了77.50% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了91.44% 的用户

解题思路：
    三指针，参考的官方解题思路：https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode/
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            min_ = min(2*dp[p2], 3*dp[p3], 5*dp[p5])
            dp[i] = min_
            if dp[p2] * 2 == min_:
                p2 += 1
            if dp[p3] * 3 == min_:
                p3 += 1
            if dp[p5] * 5 == min_:
                p5 += 1
        return dp[-1]</code></pre></div>
