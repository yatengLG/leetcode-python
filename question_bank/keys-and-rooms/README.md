<h2>841. 钥匙和房间</h2><p>有 <code>N</code> 个房间，开始时你位于 <code>0</code> 号房间。每个房间有不同的号码：<code>0，1，2，...，N-1</code>，并且房间里可能有一些钥匙能使你进入下一个房间。</p>

<p>在形式上，对于每个房间 <code>i</code> 都有一个钥匙列表 <code>rooms[i]</code>，每个钥匙 <code>rooms[i][j]</code> 由 <code>[0,1，...，N-1]</code> 中的一个整数表示，其中 <code>N = rooms.length</code>。 钥匙 <code>rooms[i][j] = v</code> 可以打开编号为 <code>v</code> 的房间。</p>

<p>最初，除 <code>0</code> 号房间外的其余所有房间都被锁住。</p>

<p>你可以自由地在房间之间来回走动。</p>

<p>如果能进入每个房间返回 <code>true</code>，否则返回 <code>false</code>。</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入: </strong>[[1],[2],[3],[]]
<strong>输出: </strong>true
<strong>解释:  </strong>
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[1,3],[3,0,1],[2],[0]]
<strong>输出：</strong>false
<strong>解释：</strong>我们不能进入 2 号房间。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= rooms.length &lt;=&nbsp;1000</code></li>
	<li><code>0 &lt;= rooms[i].length &lt;= 1000</code></li>
	<li>所有房间中的钥匙数量总计不超过&nbsp;<code>3000</code>。</li>
</ol>


 **难度**: Medium

 **标签**: 深度优先搜索、 图、 


------

<h2>841. Keys and Rooms</h2><p>There are <code>N</code> rooms and you start in room <code>0</code>.&nbsp; Each room has a distinct number in <code>0, 1, 2, ..., N-1</code>, and each room may have&nbsp;some keys to access the next room.&nbsp;</p>

<p>Formally, each room <code>i</code>&nbsp;has a list of keys <code>rooms[i]</code>, and each key <code>rooms[i][j]</code> is an integer in <code>[0, 1, ..., N-1]</code> where <code>N = rooms.length</code>.&nbsp; A key <code>rooms[i][j] = v</code>&nbsp;opens the room with number <code>v</code>.</p>

<p>Initially, all the rooms start locked (except for room <code>0</code>).&nbsp;</p>

<p>You can walk back and forth between rooms freely.</p>

<p>Return <code>true</code>&nbsp;if and only if you can enter&nbsp;every room.</p>

<ol>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1],[2],[3],[]]
<strong>Output: </strong>true
<strong>Explanation:  </strong>
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1,3],[3,0,1],[2],[0]]
<strong>Output: </strong>false
<strong>Explanation: </strong>We can&#39;t enter the room with number 2.
</pre>

<p><b>Note:</b></p>

<ol>
	<li><code>1 &lt;= rooms.length &lt;=&nbsp;1000</code></li>
	<li><code>0 &lt;= rooms[i].length &lt;= 1000</code></li>
	<li>The number of keys in all rooms combined is at most&nbsp;<code>3000</code>.</li>
</ol>


 **difficulty**: Medium

 **topic**: Depth-first Search, Graph, 

