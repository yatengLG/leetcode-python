<h2>332. 重新安排行程</h2><p>给定一个机票的字符串二维数组 <code>[from, to]</code>，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。</p>

<p><strong>说明:</strong></p>

<ol>
	<li>如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 [&quot;JFK&quot;, &quot;LGA&quot;] 与 [&quot;JFK&quot;, &quot;LGB&quot;] 相比就更小，排序更靠前</li>
	<li>所有的机场都用三个大写字母表示（机场代码）。</li>
	<li>假定所有机票至少存在一种合理的行程。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre><code><strong>输入: </strong></code><code>[[&quot;MUC&quot;, &quot;LHR&quot;], [&quot;JFK&quot;, &quot;MUC&quot;], [&quot;SFO&quot;, &quot;SJC&quot;], [&quot;LHR&quot;, &quot;SFO&quot;]]</code>
<strong>输出: </strong><code>[&quot;JFK&quot;, &quot;MUC&quot;, &quot;LHR&quot;, &quot;SFO&quot;, &quot;SJC&quot;]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre><code><strong>输入: </strong></code><code>[[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]</code>
<strong>输出: </strong><code>[&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>
<strong>解释: </strong>另一种有效的行程是&nbsp;<code>[&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>。但是它自然排序更大更靠后。</pre>


 **难度**: Medium

 **标签**: 深度优先搜索、 图、 


------

<h2>332. Reconstruct Itinerary</h2><p>Given a list of airline tickets represented by pairs of departure and arrival airports <code>[from, to]</code>, reconstruct the itinerary in order. All of the tickets belong to a man who departs from <code>JFK</code>. Thus, the itinerary must begin with <code>JFK</code>.</p>

<p><b>Note:</b></p>

<ol>
	<li>If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary <code>[&quot;JFK&quot;, &quot;LGA&quot;]</code> has a smaller lexical order than <code>[&quot;JFK&quot;, &quot;LGB&quot;]</code>.</li>
	<li>All airports are represented by three capital letters (IATA code).</li>
	<li>You may assume all tickets form at least one valid itinerary.</li>
	<li>One must use all the tickets once and only once.</li>
</ol>

<p><b>Example 1:</b></p>

<pre>
<code><strong>Input: </strong></code><code>[[&quot;MUC&quot;, &quot;LHR&quot;], [&quot;JFK&quot;, &quot;MUC&quot;], [&quot;SFO&quot;, &quot;SJC&quot;], [&quot;LHR&quot;, &quot;SFO&quot;]]</code>
<strong>Output: </strong><code>[&quot;JFK&quot;, &quot;MUC&quot;, &quot;LHR&quot;, &quot;SFO&quot;, &quot;SJC&quot;]</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<code><strong>Input: </strong></code><code>[[&quot;JFK&quot;,&quot;SFO&quot;],[&quot;JFK&quot;,&quot;ATL&quot;],[&quot;SFO&quot;,&quot;ATL&quot;],[&quot;ATL&quot;,&quot;JFK&quot;],[&quot;ATL&quot;,&quot;SFO&quot;]]</code>
<strong>Output: </strong><code>[&quot;JFK&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>
<strong>Explanation: </strong>Another possible reconstruction is <code>[&quot;JFK&quot;,&quot;SFO&quot;,&quot;ATL&quot;,&quot;JFK&quot;,&quot;ATL&quot;,&quot;SFO&quot;]</code>.
&nbsp;            But it is larger in lexical order.
</pre>


 **difficulty**: Medium

 **topic**: Depth-first Search, Graph, 

