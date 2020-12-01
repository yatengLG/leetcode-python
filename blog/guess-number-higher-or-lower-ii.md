Leetcode 375. 猜数字大小 II
<p>我们正在玩一个猜数游戏，游戏规则如下：</p>


<p>我从&nbsp;<strong>1&nbsp;</strong>到 <strong>n</strong> 之间选择一个数字，你来猜我选了哪个数字。</p>



<p>每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。</p>



<p>然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。</p>



<p><strong>示例:</strong></p>



<pre>n = 10, 我选择了8.



第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。

第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。

第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。



游戏结束。8 就是我选的数字。



你最终要支付 5 + 7 + 9 = 21 块钱。

</pre>



<p>给定&nbsp;<strong>n &ge; 1，</strong>计算你至少需要拥有多少现金才能确保你能赢得这个游戏。</p>





 **难度**: Medium



 **标签**: 极小化极大、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：608 ms, 在所有 Python3 提交中击败了71.12% 的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了80.08% 的用户

解题思路：
    动态规划。 参考了网站提供的思路 https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/solution/pythondong-tai-gui-hua-xiao-bai-ling-ji-chu-jiao-2/


        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23
    1   0   1   2   4   6   8   10  12  14  16  18  21  24  27  30  34  38  42  46  49  52  55  58
    2       0   2   3   6   8
    3           0   3   4   8
    4               0   4   5
    5                   0   5
    6                       0

    使用dp[i][j]表示， 从i~j需要的最少金钱。
        1. [i][i] = 0
            一个数字时，不需要猜
        2. [i][i+1] = i
            5~6时，猜5
        3. 对于[i][j]
            通过 dp[i][j] = min(dp[i][x-1], dp[x+1][j]) + x .  for x in range(i, j)
            也就是，将 i~j 以i~j中的某一数字为中心切成不同的片段，取前半部分切片与后半部分切片的最大值 加上该数字 作为当前切片的金钱
            将不同切片情况的最小值，作为当前i~j的最终金钱

"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n):
            dp[i][i+1] = i  # dp[i][i+1] = 1
        for j in range(1, n+1): # 这里需要注意遍历顺序。
            for i in range(j-2, 0, -1): # 忽略[i][i] 与 [i][i+1]
                dp[i][j] = min(max(dp[i][x-1], dp[x+1][j])+x for x in range(i,j))   # 状态转移方程
        return dp[1][n]
</code></pre></div>
