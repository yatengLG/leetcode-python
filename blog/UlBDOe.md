Leetcode LCP 19. 秋叶收藏集
小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。



**示例 1：**

>输入：`leaves = "rrryyyrryyyrr"`

>

>输出：`2`

>

>解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"



**示例 2：**

>输入：`leaves = "ryr"`

>

>输出：`0`

>

>解释：已符合要求，不需要额外操作



**提示：**

- `3 <= leaves.length <= 10^5`

- `leaves` 中只包含字符 `'r'` 和字符 `'y'`



 **难度**: Medium



 **标签**: 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：3020 ms, 在所有 Python3 提交中击败了5.04% 的用户
内存消耗：33 MB, 在所有 Python3 提交中击败了32.54% 的用户

解题思路：
    动态规划
    题中需要r*y*r*格式，由r*、r*y*、r*y*r*一步一步满足

        r   r   r   y   y   y   r   r   y   y   y   r   r
        0   0   0   1   2   3   3   3   4   5   6   6   6   # r*
            1   1   0   0   0   1   2   2   2   2   3   4   # r*y*
                1   2   1   1   0   0   1   2   3   2   2   # r*y*r*

        y   r   y   y   r   y
        1   1   2   3   3   4   # r*
            2   1   1   2   2   # r*y*
                3   2   1   2   # r*y*r*

"""
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        dp = [[ float('inf') for _ in range(3)]  for _ in leaves]
        dp[0][0] = int(leaves[0]!='r')
        for i in range(1, len(leaves)):
            dp[i][0] = dp[i-1][0] + int(leaves[i]!='r')                     # r* 只依赖于 r*情况
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(leaves[i]!='y')    # r*y* 可由 r*+y 和r*y*+y 得到，依赖于 r* 和r*y*情况
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + int(leaves[i]!='r')    # r*y*r* 可由 r*y*+r 和 r*y*r*+r 得到，依赖于r*y* 和 r*y*r*情况
        return dp[-1][2]</code></pre></div>
