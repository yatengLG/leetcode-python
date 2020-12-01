Leetcode 96. 不同的二叉搜索树
<p>给定一个整数 <em>n</em>，求以&nbsp;1 ...&nbsp;<em>n</em>&nbsp;为节点组成的二叉搜索树有多少种？</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> 3

<strong>输出:</strong> 5

<strong>解释:

</strong>给定 <em>n</em> = 3, 一共有 5 种不同结构的二叉搜索树:



   1         3     3      2      1

    \       /     /      / \      \

     3     2     1      1   3      2

    /     /       \                 \

   2     1         2                 3</pre>





 **难度**: Medium



 **标签**: 树、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了85.19% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.17% 的用户

解题思路：
    当前以j为根的树的种类 = 左子树的种类* 右子树的种类
        n   class   [左子树节点数,右子树节点数]
        0   1
        1   1       [0,1]                           1*1
        2   2       [0,1] [1,0]                     1*1 + 1*1
        3   5       [0,2] [1,1] [2,0]               1*2 + 1*1 + 2*1
        4   14      [0,3] [1,2] [2,1] [3,0]         1*5 + 1*2 + 2*1 + 5*1
        5   42      [0,4] [1,3] [2,2] [3,1] [4,0]   1*14 + 1*5 + 2*2 + 5*1 + 14*1
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):     # n
            for j in range(1, i+1): # 当前n时，以j为根的树有 左子树种类*右子树种类 种
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]</code></pre></div>
