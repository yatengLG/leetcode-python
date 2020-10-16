<h2>134. 加油站</h2><p>在一条环路上有&nbsp;<em>N</em>&nbsp;个加油站，其中第&nbsp;<em>i</em>&nbsp;个加油站有汽油&nbsp;<code>gas[i]</code><em>&nbsp;</em>升。</p>

<p>你有一辆油箱容量无限的的汽车，从第<em> i </em>个加油站开往第<em> i+1&nbsp;</em>个加油站需要消耗汽油&nbsp;<code>cost[i]</code><em>&nbsp;</em>升。你从其中的一个加油站出发，开始时油箱为空。</p>

<p>如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。</p>

<p><strong>说明:</strong>&nbsp;</p>

<ul>
	<li>如果题目有解，该答案即为唯一答案。</li>
	<li>输入数组均为非空数组，且长度相同。</li>
	<li>输入数组中的元素均为非负数。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

<strong>输出:</strong> 3

<strong>解释:
</strong>从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 
gas  = [2,3,4]
cost = [3,4,3]

<strong>输出:</strong> -1

<strong>解释:
</strong>你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。</pre>


 **难度**: Medium

 **标签**: 贪心算法、 


------

<h2>134. Gas Station</h2><p>There are <em>N</em> gas stations along a circular route, where the amount of gas at station <em>i</em> is <code>gas[i]</code>.</p>

<p>You have a car with an unlimited gas tank and it costs <code>cost[i]</code> of gas to travel from station <em>i</em> to its next station (<em>i</em>+1). You begin the journey with an empty tank at one of the gas stations.</p>

<p>Return the starting gas station&#39;s index if you can travel around the circuit once in the clockwise direction, otherwise return -1.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>If there exists a&nbsp;solution, it is guaranteed to be unique.</li>
	<li>Both input arrays are non-empty and have the same length.</li>
	<li>Each element in the input arrays is a non-negative integer.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

<strong>Output:</strong> 3

<strong>Explanation:
</strong>Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
gas  = [2,3,4]
cost = [3,4,3]

<strong>Output:</strong> -1

<strong>Explanation:
</strong>You can&#39;t start at station 0 or 1, as there is not enough gas to travel to the next station.
Let&#39;s start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can&#39;t travel around the circuit once no matter where you start.
</pre>


 **difficulty**: Medium

 **topic**: Greedy, 

