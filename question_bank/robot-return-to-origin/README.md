<h2>657. 机器人能否返回原点</h2><p>在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在<strong>&nbsp;(0, 0) 处结束</strong>。</p>

<p>移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有&nbsp;<code>R</code>（右），<code>L</code>（左），<code>U</code>（上）和 <code>D</code>（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。</p>

<p><strong>注意：</strong>机器人&ldquo;面朝&rdquo;的方向无关紧要。 &ldquo;R&rdquo; 将始终使机器人向右移动一次，&ldquo;L&rdquo; 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;UD&quot;
<strong>输出:</strong> true
<strong>解释：</strong>机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot;LL&quot;
<strong>输出:</strong> false
<strong>解释：</strong>机器人向左移动两次。它最终位于原点的左侧，距原点有两次 &ldquo;移动&rdquo; 的距离。我们返回 false，因为它在移动结束时没有返回原点。</pre>


 **难度**: Easy

 **标签**: 字符串、 


------

<h2>657. Robot Return to Origin</h2><p>There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot <strong>ends up at (0, 0)</strong> after it completes its moves.</p>

<p>The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.</p>

<p><strong>Note</strong>: The way that the robot is &quot;facing&quot; is irrelevant. &quot;R&quot; will always make the robot move to the right once, &quot;L&quot; will always make it move left, etc. Also, assume that the magnitude of the robot&#39;s movement is the same for each move.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;UD&quot;
<b>Output:</b> true 
<strong>Explanation</strong>: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;LL&quot;
<b>Output:</b> false
<strong>Explanation</strong>: The robot moves left twice. It ends up two &quot;moves&quot; to the left of the origin. We return false because it is not at the origin at the end of its moves.
</pre>


 **difficulty**: Easy

 **topic**: String, 

