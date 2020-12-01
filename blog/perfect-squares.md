Leetcode 279. 完全平方数
<p>给定正整数&nbsp;<em>n</em>，找到若干个完全平方数（比如&nbsp;<code>1, 4, 9, 16, ...</code>）使得它们的和等于<em> n</em>。你需要让组成和的完全平方数的个数最少。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> <em>n</em> = <code>12</code>

<strong>输出:</strong> 3 

<strong>解释: </strong><code>12 = 4 + 4 + 4.</code></pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> <em>n</em> = <code>13</code>

<strong>输出:</strong> 2

<strong>解释: </strong><code>13 = 4 + 9.</code></pre>





 **难度**: Medium



 **标签**: 广度优先搜索、 数学、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：208 ms, 在所有 Python3 提交中击败了86.90% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了79.52% 的用户

解题思路：
    贪心算法
    参考了官方思路：  https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode/

    把一个数，拆成，完全平方数，要求组成的数的数量最少
    改为求一个数，可不可以由count个 完全平方数组成
    由此得到该数的最少的完全平方数数量

    具体思路见代码注释
"""
class Solution:
    def numSquares(self, n: int) -> int:
        def f(num, count):  # 定义一个函数，如 num 可以由count个完全平方数组成，则返回True
            if count == 1:
                return num in square_nums   # 单个完全平方数构成的数，也在完全平方数里

            for k in square_nums:       # 当前数，减去一个完全平方数后，看是否可以由 count-1个 完全平方数构成
                if f(num-k, count-1):
                    return True
            return False

        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]   # 完全平方数
        for count in range(1, n + 1):   # 从 1 到n，看可以由多少个完全平方数构成。
            if f(n, count):
                return count</code></pre></div>
