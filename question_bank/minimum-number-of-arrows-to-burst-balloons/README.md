<h2>452. 用最少数量的箭引爆气球</h2><p>在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。</p>

<p>一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 <code>x</code><sub><code>start</code>，</sub><code>x</code><sub><code>end</code>，</sub> 且满足  <code>x<sub>start</sub> ≤ x ≤ x</code><sub><code>end</code>，</sub>则该气球会被引爆<sub>。</sub>可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。</p>

<p>给你一个数组 <code>points</code> ，其中 <code>points [i] = [x<sub>start</sub>,x<sub>end</sub>]</code> ，返回引爆所有气球所必须射出的最小弓箭数。</p>
 

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>points = [[10,16],[2,8],[1,6],[7,12]]
<strong>输出：</strong>2
<strong>解释：</strong>对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,2],[3,4],[5,6],[7,8]]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,2],[2,3],[3,4],[4,5]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>points = [[1,2]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>points = [[2,3],[2,3]]
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= points.length <= 10<sup>4</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-2<sup>31</sup> <= x<sub>start</sub> < x<sub>end</sub> <= 2<sup>31</sup> - 1</code></li>
</ul>


 **难度**: Medium

 **标签**: 贪心算法、 排序、 


------

<h2>452. Minimum Number of Arrows to Burst Balloons</h2><p>There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it&#39;s horizontal, y-coordinates don&#39;t matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.</p>

<p>An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> bursts by an arrow shot at <code>x</code> if <code>x<sub>start</sub> &le; x &le; x<sub>end</sub></code>. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.</p>

<p>Given an array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code>, return&nbsp;<em>the minimum number of arrows that must be shot to burst all balloons</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong>Output:</strong> 4
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong>Output:</strong> 2
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,2]]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> points = [[2,3],[2,3]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= points.length &lt;= 10<sup>4</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-2<sup>31</sup> &lt;= x<sub>start</sub> &lt;&nbsp;x<sub>end</sub> &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Greedy, Sort, 

