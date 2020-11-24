<h2>406. 根据身高重建队列</h2><p>假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 <code>(h, k)</code> 表示，其中 <code>h</code> 是这个人的身高，<code>k</code> 是应该排在这个人前面且身高大于或等于 <code>h</code> 的人数。 例如：[5,2] 表示前面应该有 2 个身高大于等于 5 的人，而 [5,0] 表示前面不应该存在身高大于等于 5 的人。</p>

<p>编写一个算法，根据每个人的身高 <code>h</code> 重建这个队列，使之满足每个整数对 <code>(h, k)</code> 中对人数 <code>k</code> 的要求。</p>

<ul>
</ul>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
<strong>输出：</strong>[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>总人数少于 1100 人。</li>
</ul>


 **难度**: Medium

 **标签**: 贪心算法、 


------

<h2>406. Queue Reconstruction by Height</h2><p>You are given an array of people, <code>people</code>, which are the attributes of some people in a queue (not necessarily in order). Each <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> person of height <code>h<sub>i</sub></code> with <strong>exactly</strong> <code>k<sub>i</sub></code> other people in front who have a height greater than or equal to <code>h<sub>i</sub></code>.</p>

<p>Reconstruct and return <em>the queue that is represented by the input array </em><code>people</code>. The returned queue should be formatted as an array <code>queue</code>, where <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> is the attributes of the <code>j<sup>th</sup></code> person in the queue (<code>queue[0]</code> is the person at the front of the queue).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>Output:</strong> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>Explanation:</strong>
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with one person taller or the same height in front, which is person 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>Output:</strong> [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 2000</code></li>
	<li><code>0 &lt;= h<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k<sub>i</sub> &lt; people.length</code></li>
	<li>It is guaranteed that the queue can be reconstructed.</li>
</ul>


 **difficulty**: Medium

 **topic**: Greedy, 

