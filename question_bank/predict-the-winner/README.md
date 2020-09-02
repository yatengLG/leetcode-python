<h2>486. 预测赢家</h2><p>给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，&hellip;&hellip; 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。</p>

<p>给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1, 5, 2]
<strong>输出：</strong>False
<strong>解释：</strong>一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1, 5, 233, 7]
<strong>输出：</strong>True
<strong>解释：</strong>玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>1 &lt;= 给定的数组长度&nbsp;&lt;= 20.</li>
	<li>数组里所有分数都为非负数且不会大于 10000000 。</li>
	<li>如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。</li>
</ul>


 **难度**: Medium

 **标签**: 极小化极大、 动态规划、 


------

<h2>486. Predict the Winner</h2><p>Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.</p>

<p>Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1, 5, 2]
<b>Output:</b> False
<b>Explanation:</b> Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1, 5, 233, 7]
<b>Output:</b> True
<b>Explanation:</b> Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>1 &lt;= length of the array &lt;= 20.</li>
	<li>Any scores in the given array are non-negative integers and will not exceed 10,000,000.</li>
	<li>If the scores of both players are equal, then player 1 is still the winner.</li>
</ul>


 **difficulty**: Medium

 **topic**: Minimax, Dynamic Programming, 

