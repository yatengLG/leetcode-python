Leetcode 122. 买卖股票的最佳时机 II
<p>给定一个数组，它的第&nbsp;<em>i</em> 个元素是一支给定股票第 <em>i</em> 天的价格。</p>


<p>设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。</p>



<p><strong>注意：</strong>你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>



<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [7,1,5,3,6,4]

<strong>输出:</strong> 7

<strong>解释:</strong> 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。

&nbsp;    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> [1,2,3,4,5]

<strong>输出:</strong> 4

<strong>解释:</strong> 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。

&nbsp;    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。

&nbsp;    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

</pre>



<p><strong>示例&nbsp;3:</strong></p>



<pre><strong>输入:</strong> [7,6,4,3,1]

<strong>输出:</strong> 0

<strong>解释:</strong> 在这种情况下, 没有交易完成, 所以最大利润为 0。</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= prices.length &lt;= 3 * 10 ^ 4</code></li>

	<li><code>0 &lt;= prices[i]&nbsp;&lt;= 10 ^ 4</code></li>

</ul>





 **难度**: Easy



 **标签**: 贪心算法、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了39.51% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了58.55% 的用户

解题思路：
    贪心算法
    每次只求当前局部最优解。
    每当股价上升时，就将上升的幅度计入总利润， 最终得到的便是最大总利润
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        for i in range(n-1):
            result += max(prices[i + 1] - prices[i], 0)
        return result
</code></pre></div>
