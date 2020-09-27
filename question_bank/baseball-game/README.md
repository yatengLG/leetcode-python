<h2>682. 棒球比赛</h2><p>你现在是棒球比赛记录员。<br>
给定一个字符串列表，每个字符串可以是以下四种类型之一：<br>
1.<code>整数</code>（一轮的得分）：直接表示您在本轮中获得的积分数。<br>
2. <code>&quot;+&quot;</code>（一轮的得分）：表示本轮获得的得分是前两轮<code>有效</code>&nbsp;回合得分的总和。<br>
3. <code>&quot;D&quot;</code>（一轮的得分）：表示本轮获得的得分是前一轮<code>有效</code>&nbsp;回合得分的两倍。<br>
4. <code>&quot;C&quot;</code>（一个操作，这不是一个回合的分数）：表示您获得的最后一个<code>有效</code>&nbsp;回合的分数是无效的，应该被移除。<br>
<br>
每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。<br>
你需要返回你在所有回合中得分的总和。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [&quot;5&quot;,&quot;2&quot;,&quot;C&quot;,&quot;D&quot;,&quot;+&quot;]
<strong>输出:</strong> 30
<strong>解释:</strong> 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到2分。总和是：7。
操作1：第2轮的数据无效。总和是：5。
第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
第4轮：你可以得到5 + 10 = 15分。总数是：30。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [&quot;5&quot;,&quot;-2&quot;,&quot;4&quot;,&quot;C&quot;,&quot;D&quot;,&quot;9&quot;,&quot;+&quot;,&quot;+&quot;]
<strong>输出:</strong> 27
<strong>解释:</strong> 
第1轮：你可以得到5分。总和是：5。
第2轮：你可以得到-2分。总数是：3。
第3轮：你可以得到4分。总和是：7。
操作1：第3轮的数据无效。总数是：3。
第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
第5轮：你可以得到9分。总数是：8。
第6轮：你可以得到-4 + 9 = 5分。总数是13。
第7轮：你可以得到9 + 5 = 14分。总数是27。
</pre>

<p><strong>注意：</strong></p>

<ul>
	<li>输入列表的大小将介于1和1000之间。</li>
	<li>列表中的每个整数都将介于-30000和30000之间。</li>
</ul>


 **难度**: Easy

 **标签**: 栈、 


------

<h2>682. Baseball Game</h2><p>
You're now a baseball game point recorder.
</p>

<p>
Given a list of strings, each string can be one of the 4 following types:
<ol>
<li><code>Integer</code> (one round's score): Directly represents the number of points you get in this round.</li>
<li><code>"+"</code> (one round's score): Represents that the points you get in this round are the sum of the last two <code>valid</code> round's points.</li>
<li><code>"D"</code> (one round's score): Represents that the points you get in this round are the doubled data of the last <code>valid</code> round's points.</li>
<li><code>"C"</code> (an operation, which isn't a round's score): Represents the last <code>valid</code> round's points you get were invalid and should be removed.</li>
</ol>
</p>

<p>
Each round's operation is permanent and could have an impact on the round before and the round after.
</p>

<p>
You need to return the sum of the points you could get in all the rounds.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> ["5","2","C","D","+"]
<b>Output:</b> 30
<b>Explanation:</b> 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.  
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> ["5","-2","4","C","D","9","+","+"]
<b>Output:</b> 27
<b>Explanation:</b> 
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3's data is invalid. The sum is: 3.  
Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.
</pre>
</p>

<p><b>Note:</b><br />
<li>The size of the input list will be between 1 and 1000.</li>
<li>Every integer represented in the list will be between -30000 and 30000.</li>
</p>

 **difficulty**: Easy

 **topic**: Stack, 

