<h2>52. N皇后 II</h2><p><em>n&nbsp;</em>皇后问题研究的是如何将 <em>n</em>&nbsp;个皇后放置在 <em>n</em>&times;<em>n</em> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png" style="height: 276px; width: 258px;"></p>

<p><small>上图为 8 皇后问题的一种解法。</small></p>

<p>给定一个整数 <em>n</em>，返回 <em>n</em> 皇后不同的解决方案的数量。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 4
<strong>输出:</strong> 2
<strong>解释:</strong> 4 皇后问题存在如下两个不同的解法。
[
&nbsp;[&quot;.Q..&quot;, &nbsp;// 解法 1
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;..Q.&quot;],

&nbsp;[&quot;..Q.&quot;, &nbsp;// 解法 2
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;.Q..&quot;]
]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><strong>皇后</strong>，是<a href="https://baike.baidu.com/item/%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B" target="_blank">国际象棋</a>中的棋子，意味着<a href="https://baike.baidu.com/item/%E5%9B%BD%E7%8E%8B" target="_blank">国王</a>的妻子。皇后只做一件事，那就是&ldquo;<a href="https://baike.baidu.com/item/%E5%90%83%E5%AD%90" target="_blank">吃子</a>&rdquo;。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N-1 步，可进可退。（引用自 <a href="https://baike.baidu.com/item/%E7%9A%87%E5%90%8E/15860305?fr=aladdin">百度百科 - 皇后</a> ）</li>
</ul>


 **难度**: Hard

 **标签**: 回溯算法、 


------

<h2>52. N-Queens II</h2><p>The <em>n</em>-queens puzzle is the problem of placing <em>n</em> queens on an <em>n</em>&times;<em>n</em> chessboard such that no two queens attack each other.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" style="width: 258px; height: 276px;" /></p>

<p>Given an integer&nbsp;<em>n</em>, return the number of&nbsp;distinct solutions to the&nbsp;<em>n</em>-queens puzzle.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two distinct solutions to the 4-queens puzzle as shown below.
[
&nbsp;[&quot;.Q..&quot;, &nbsp;// Solution 1
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;..Q.&quot;],

&nbsp;[&quot;..Q.&quot;, &nbsp;// Solution 2
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;.Q..&quot;]
]
</pre>


 **difficulty**: Hard

 **topic**: Backtracking, 

