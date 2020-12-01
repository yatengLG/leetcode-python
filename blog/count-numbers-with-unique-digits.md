Leetcode 357. 计算各个位数不同的数字个数
<p>给定一个<strong>非负</strong>整数 n，计算各位数字都不同的数字 x 的个数，其中 0 &le; x &lt; 10<sup>n&nbsp;</sup>。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入: </strong>2

<strong>输出: </strong>91 

<strong>解释: </strong>答案应为除去 <code>11,22,33,44,55,66,77,88,99 </code>外，在 [0,100) 区间内的所有数字。

</pre>





 **难度**: Medium



 **标签**: 数学、 动态规划、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了85.03% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了93.39% 的用户

解题思路：
    动态规划
        0 <= x < 10**n, x为最大n位数
        m       num             说明
        1位数     10          0,1~9
        2位数     9*9         第一位9个：1~9 第二位10-1个：0~9
        3位数     9*9*8       第一位9个：1~9 第二位10-1个：0~9 第三位10-2个0~9
        4位数     9*9*8*7     第一位9个：1~9 第二位10-1个：0~9 第三位10-2个0~9 第四位10-3个0~9
        5位数     9*9*8*7*6
        6位数     9*9*8*7*6*5
        7位数     9*9*8*7*6*5*4
        8位数     9*9*8*7*6*5*4*3
        9位数     9*9*8*7*6*5*4*3*2
        10位数    9*9*8*7*6*5*4*3*2*1
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [0 for _ in range(10)]
        dp[:3] = [1, 9, 81]
        for i in range(3,10):
            dp[i] = dp[i-1]*(10-i+1)
        if n > 9:
            n = 9
        return sum(dp[:n+1])
</code></pre></div>
