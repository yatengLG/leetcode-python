<h2>1024. 视频拼接</h2><p>你将会获得一系列视频片段，这些片段来自于一项持续时长为 <code>T</code> 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。</p>

<p>视频片段 <code>clips[i]</code> 都用区间进行表示：开始于 <code>clips[i][0]</code> 并于 <code>clips[i][1]</code> 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 <code>[0, 7]</code> 可以剪切成 <code>[0, 1] + [1, 3] + [3, 7]</code> 三部分。</p>

<p>我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（<code>[0, T]</code>）。返回所需片段的最小数目，如果无法完成该任务，则返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
<strong>输出：</strong>3
<strong>解释：</strong>
我们选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,1],[1,2]], T = 5
<strong>输出：</strong>-1
<strong>解释：</strong>
我们无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
<strong>输出：</strong>3
<strong>解释： </strong>
我们选取片段 [0,4], [4,7] 和 [6,9] 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>clips = [[0,4],[2,8]], T = 5
<strong>输出：</strong>2
<strong>解释：</strong>
注意，你可能录制超过比赛结束时间的视频。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= clips.length <= 100</code></li>
	<li><code>0 <= clips[i][0] <= clips[i][1] <= 100</code></li>
	<li><code>0 <= T <= 100</code></li>
</ul>


 **难度**: Medium

 **标签**: 动态规划、 


------

<h2>1024. Video Stitching</h2><p>You are given a series of video clips from a sporting event that lasted <code>T</code> seconds.&nbsp;&nbsp;These video clips can be overlapping with each other and have varied lengths.</p>

<p>Each video clip <code>clips[i]</code>&nbsp;is an interval: it starts at time <code>clips[i][0]</code> and ends at time <code>clips[i][1]</code>.&nbsp; We can cut these clips into segments freely: for example, a clip <code>[0, 7]</code> can be cut into segments&nbsp;<code>[0, 1] +&nbsp;[1, 3] + [3, 7]</code>.</p>

<p>Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event (<code>[0, T]</code>).&nbsp; If the task is impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>clips = <span id="example-input-1-1">[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]</span>, T = <span id="example-input-1-2">10</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>clips = <span id="example-input-2-1">[[0,1],[1,2]]</span>, T = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>
We can&#39;t cover [0,5] with only [0,1] and [1,2].
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>clips = <span id="example-input-3-1">[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]</span>, T = <span id="example-input-3-2">9</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong>
We can take clips [0,4], [4,7], and [6,9].
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>clips = <span id="example-input-4-1">[[0,4],[2,8]]</span>, T = <span id="example-input-4-2">5</span>
<strong>Output: </strong><span id="example-output-4">2</span>
<strong>Explanation: </strong>
Notice you can have extra video after the event ends.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= clips.length &lt;= 100</code></li>
	<li><code>0 &lt;= clips[i][0] &lt;=&nbsp;clips[i][1] &lt;= 100</code></li>
	<li><code>0 &lt;= T &lt;= 100</code></li>
</ul>


 **difficulty**: Medium

 **topic**: Dynamic Programming, 

