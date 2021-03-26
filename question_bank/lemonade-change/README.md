<h2>860. 柠檬水找零</h2><p>在柠檬水摊上，每一杯柠檬水的售价为&nbsp;<code>5</code>&nbsp;美元。</p>

<p>顾客排队购买你的产品，（按账单 <code>bills</code> 支付的顺序）一次购买一杯。</p>

<p>每位顾客只买一杯柠檬水，然后向你付 <code>5</code> 美元、<code>10</code> 美元或 <code>20</code> 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 <code>5</code> 美元。</p>

<p>注意，一开始你手头没有任何零钱。</p>

<p>如果你能给每位顾客正确找零，返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[5,5,5,10,20]
<strong>输出：</strong>true
<strong>解释：
</strong>前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[5,5,10]
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[10,10]
<strong>输出：</strong>false
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>[5,5,10,10,20]
<strong>输出：</strong>false
<strong>解释：</strong>
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= bills.length &lt;= 10000</code></li>
	<li><code>bills[i]</code>&nbsp;不是&nbsp;<code>5</code>&nbsp;就是&nbsp;<code>10</code>&nbsp;或是&nbsp;<code>20</code>&nbsp;</li>
</ul>


 **难度**: Easy

 **标签**: 贪心算法、 


------

<h2>860. Lemonade Change</h2><p>At a lemonade stand, each lemonade costs <code>$5</code>.&nbsp;</p>

<p>Customers are standing in a queue to buy from you, and order one at a time (in the order specified by <code>bills</code>).</p>

<p>Each customer will only buy one lemonade and&nbsp;pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill.&nbsp; You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.</p>

<p>Note that you don&#39;t have any change&nbsp;in hand at first.</p>

<p>Return <code>true</code>&nbsp;if and only if you can provide every customer with correct change.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,5,5,10,20]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,5,10]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[10,10]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[5,5,10,10,20]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
<strong>Explanation: </strong>
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can't give change of $15 back because we only have two $10 bills.
Since not every customer received correct change, the answer is false.
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><code>0 &lt;= bills.length &lt;= 10000</code></li>
	<li><code>bills[i]</code>&nbsp;will be either&nbsp;<code>5</code>, <code>10</code>, or <code>20</code>.</li>
</ul>
</div>
</div>
</div>
</div>


 **difficulty**: Easy

 **topic**: Greedy, 

