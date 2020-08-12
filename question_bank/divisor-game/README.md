<h2>1025. 除数博弈</h2><p>爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。</p>

<p>最初，黑板上有一个数字&nbsp;<code>N</code>&nbsp;。在每个玩家的回合，玩家需要执行以下操作：</p>

<ul>
	<li>选出任一&nbsp;<code>x</code>，满足&nbsp;<code>0 &lt; x &lt; N</code> 且&nbsp;<code>N % x == 0</code>&nbsp;。</li>
	<li>用 <code>N - x</code>&nbsp;替换黑板上的数字 <code>N</code> 。</li>
</ul>

<p>如果玩家无法执行这些操作，就会输掉游戏。</p>

<p>只有在爱丽丝在游戏中取得胜利时才返回&nbsp;<code>True</code>，否则返回 <code>False</code>。假设两个玩家都以最佳状态参与游戏。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>2
<strong>输出：</strong>true
<strong>解释：</strong>爱丽丝选择 1，鲍勃无法进行操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>3
<strong>输出：</strong>false
<strong>解释：</strong>爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000</code></li>
</ol>
 难度: Easy

 标签: 数学、 动态规划、 


------

<h2>1025. Divisor Game</h2><p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>Initially, there is a number <code>N</code>&nbsp;on the chalkboard.&nbsp; On each player&#39;s turn, that player makes a <em>move</em>&nbsp;consisting of:</p>

<ul>
	<li>Choosing&nbsp;any <code>x</code> with <code>0 &lt; x &lt; N</code> and <code>N % x == 0</code>.</li>
	<li>Replacing&nbsp;the number&nbsp;<code>N</code>&nbsp;on the chalkboard with <code>N - x</code>.</li>
</ul>

<p>Also, if a player cannot make a move, they lose the game.</p>

<p>Return <code>True</code> if and only if Alice wins the game, assuming both players play optimally.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation:</strong> Alice chooses 1, and Bob has no more moves.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">3</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation:</strong> Alice chooses 1, Bob chooses 1, and Alice has no more moves.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 1000</code></li>
</ol>
</div>
</div>
------

 difficulty: Easy

 topic: Math, Dynamic Programming, 

