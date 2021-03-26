<h2>714. 买卖股票的最佳时机含手续费</h2><p>给定一个整数数组&nbsp;<code>prices</code>，其中第&nbsp;<code>i</code>&nbsp;个元素代表了第&nbsp;<code>i</code>&nbsp;天的股票价格 ；非负整数&nbsp;<code>fee</code> 代表了交易股票的手续费用。</p>

<p>你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。</p>

<p>返回获得利润的最大值。</p>

<p><strong>注意：</strong>这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> prices = [1, 3, 2, 8, 4, 9], fee = 2
<strong>输出:</strong> 8
<strong>解释:</strong> 能够达到的最大利润:  
在此处买入&nbsp;prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:&nbsp;((8 - 1) - 2) + ((9 - 4) - 2) = 8.</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>0 &lt; prices.length &lt;= 50000</code>.</li>
	<li><code>0 &lt; prices[i] &lt; 50000</code>.</li>
	<li><code>0 &lt;= fee &lt; 50000</code>.</li>
</ul>


 **难度**: Medium

 **标签**: 贪心算法、 数组、 动态规划、 


------

<h2>714. Best Time to Buy and Sell Stock with Transaction Fee</h2><p>Your are given an array of integers <code>prices</code>, for which the <code>i</code>-th element is the price of a given stock on day <code>i</code>; and a non-negative integer <code>fee</code> representing a transaction fee.</p>
<p>You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)</p>
<p>Return the maximum profit you can make.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> prices = [1, 3, 2, 8, 4, 9], fee = 2
<b>Output:</b> 8
<b>Explanation:</b> The maximum profit can be achieved by:
<li>Buying at prices[0] = 1</li><li>Selling at prices[3] = 8</li><li>Buying at prices[4] = 4</li><li>Selling at prices[5] = 9</li>The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < prices.length <= 50000</code>.</li>
<li><code>0 < prices[i] < 50000</code>.</li>
<li><code>0 <= fee < 50000</code>.</li>
</p>

 **difficulty**: Medium

 **topic**: Greedy, Array, Dynamic Programming, 

