Leetcode 60. 第k个排列
<p>给出集合&nbsp;<code>[1,2,3,&hellip;,<em>n</em>]</code>，其所有元素共有&nbsp;<em>n</em>! 种排列。</p>


<p>按大小顺序列出所有排列情况，并一一标记，当&nbsp;<em>n </em>= 3 时, 所有排列如下：</p>



<ol>

	<li><code>&quot;123&quot;</code></li>

	<li><code>&quot;132&quot;</code></li>

	<li><code>&quot;213&quot;</code></li>

	<li><code>&quot;231&quot;</code></li>

	<li><code>&quot;312&quot;</code></li>

	<li><code>&quot;321&quot;</code></li>

</ol>



<p>给定&nbsp;<em>n</em> 和&nbsp;<em>k</em>，返回第&nbsp;<em>k</em>&nbsp;个排列。</p>



<p><strong>说明：</strong></p>



<ul>

	<li>给定<em> n</em>&nbsp;的范围是 [1, 9]。</li>

	<li>给定 <em>k&nbsp;</em>的范围是[1, &nbsp;<em>n</em>!]。</li>

</ul>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> n = 3, k = 3

<strong>输出:</strong> &quot;213&quot;

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> n = 4, k = 9

<strong>输出:</strong> &quot;2314&quot;

</pre>





 **难度**: Medium



 **标签**: 数学、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
超时

解题思路：
    回溯
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []

        def backtrack(current:list, used:list):
            if len(current) == n:
                result.append(current[:])
            for i in range(1, n+1):
                if i not in used:
                    current.append(i)
                    used.append(i)
                    backtrack(current, used)
                    current.pop()
                    used.pop()
        backtrack([], [])
        return ''.join([str(i) for i in result[k-1]])


"""
执行用时：6032 ms, 在所有 Python3 提交中击败了5.03% 的用户
内存消耗：31.5 MB, 在所有 Python3 提交中击败了6.66% 的用户

解题思路：
    指定起始首字符回溯
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        nums = 1
        for i in range(1, n):
            nums *= i
        start = (k-1) // (nums)+1
        extra = (k-1) % nums

        def backtrack(current:list, used:list):
            if len(current) == n:
                result.append(current[:])
            for i in range(1, n+1):
                if i not in used:
                    current.append(i)
                    used.append(i)
                    backtrack(current, used)
                    current.pop()
                    used.pop()

        backtrack([start], [start])
        return ''.join([str(i) for i in result[extra]])


"""
执行用时：36 ms, 在所有 Python3 提交中击败了93.06% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了84.55% 的用户

解题思路：
    例子：
            4 9 
    
        4   8//(3*2*1) = 1      1234    2
            8%(3*2*1)  = 2      
        3   2//(2*1)   = 1      134     3
            2%(2*1)    = 0      
        2   0%1        = 0      14      1
            0//1       = 0      
        1   0          = 0      4       4
        
            4 23 
    
        4   22//(3*2*1)= 3      1234    4
            22%(3*2*1) = 4      
        3   4//(2*1)   = 2      123     3
            4%(2*1)    = 0      
        2   0%1        = 0      12      1
            0//1       = 0      
        1   0          = 0      2       2
        
            3   3
        3   2//(2*1)    = 1     123     2
            2%(2*1)     = 0
        2   0//1        = 0     13      1
            0%1         = 0
        1   0           = 0     3       3

"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        nums = list(range(1, n+1))
        mul = 1
        for i in nums:
           mul *= i
        k = k-1
        for i in range(n, 0, -1):
            mul = mul / i
            index = int(k // mul)
            result.append(nums[index])
            k = k % mul
            del nums[index]

        return ''.join([str(i) for i in result])</code></pre></div>
