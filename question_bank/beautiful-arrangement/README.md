<h2>526. 优美的排列</h2><p>假设有从 1 到 N 的&nbsp;<strong>N&nbsp;</strong>个整数，如果从这&nbsp;<strong>N&nbsp;</strong>个数字中成功构造出一个数组，使得数组的第 <strong>i</strong>&nbsp;位 (1 &lt;= i &lt;= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：</p>

<ol>
	<li>第&nbsp;<strong>i&nbsp;</strong>位的数字能被&nbsp;<strong>i&nbsp;</strong>整除</li>
	<li><strong>i</strong> 能被第 <strong>i</strong> 位上的数字整除</li>
</ol>

<p>现在给定一个整数 N，请问可以构造多少个优美的排列？</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入:</strong> 2
<strong>输出:</strong> 2
<strong>解释:</strong> 

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><strong>N</strong> 是一个正整数，并且不会超过15。</li>
</ol>


 **难度**: Medium

 **标签**: 回溯算法、 


------

<h2>526. Beautiful Arrangement</h2><p>Suppose you have <b>N</b> integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these <b>N</b> numbers successfully if one of the following is true for the i<sub>th</sub> position (1 &lt;= i &lt;= N) in this array:</p>

<ol>
	<li>The number at the i<sub>th</sub> position is divisible by <b>i</b>.</li>
	<li><b>i</b> is divisible by the number at the i<sub>th</sub> position.</li>
</ol>

<p>&nbsp;</p>

<p>Now given N, how many beautiful arrangements can you construct?</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 2
<b>Output:</b> 2
<b>Explanation:</b> 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li><b>N</b> is a positive integer and will not exceed 15.</li>
</ol>

<p>&nbsp;</p>


 **difficulty**: Medium

 **topic**: Backtracking, 

