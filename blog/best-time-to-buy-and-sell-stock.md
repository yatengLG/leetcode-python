Leetcode 121. 买卖股票的最佳时机
<p>给定一个数组，它的第&nbsp;<em>i</em> 个元素是一支给定股票第 <em>i</em> 天的价格。</p>


<p>如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。</p>



<p>注意：你不能在买入股票前卖出股票。</p>



<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [7,1,5,3,6,4]

<strong>输出:</strong> 5

<strong>解释: </strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。

     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [7,6,4,3,1]

<strong>输出:</strong> 0

<strong>解释: </strong>在这种情况下, 没有交易完成, 所以最大利润为 0。

</pre>





 **难度**: Easy



 **标签**: 数组、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了95.92% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了41.17% 的用户

解题思路：
    记录当前最小值，作为买入时机，依次更新买入时机并计算利润
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices[1:]:
            if buy > price:
                buy = price
            else:
                profit = max((price-buy), profit)
        return profit
</code></pre></div>
