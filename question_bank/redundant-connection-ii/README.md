<h2>685. 冗余连接 II</h2><p>在本问题中，有根树指满足以下条件的<strong>有向</strong>图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。</p>

<p>输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。</p>

<p>结果图是一个以<code>边</code>组成的二维数组。 每一个<code>边</code> 的元素是一对 <code>[u, v]</code>，用以表示<strong>有向</strong>图中连接顶点 <code>u</code> 和顶点 <code>v</code> 的边，其中 <code>u</code> 是 <code>v</code> 的一个父节点。</p>

<p>返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> [[1,2], [1,3], [2,3]]
<strong>输出:</strong> [2,3]
<strong>解释:</strong> 给定的有向图如下:
  1
 / \
v   v
2--&gt;3
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [[1,2], [2,3], [3,4], [4,1], [1,5]]
<strong>输出:</strong> [4,1]
<strong>解释:</strong> 给定的有向图如下:
5 &lt;- 1 -&gt; 2
     ^    |
     |    v
     4 &lt;- 3
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>二维数组大小的在3到1000范围内。</li>
	<li>二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。</li>
</ul>


 **难度**: Hard

 **标签**: 树、 深度优先搜索、 并查集、 图、 


------

<h2>685. Redundant Connection II</h2><p>
In this problem, a rooted tree is a <b>directed</b> graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
</p><p>
The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
</p><p>
The resulting graph is given as a 2D-array of <code>edges</code>.  Each element of <code>edges</code> is a pair <code>[u, v]</code> that represents a <b>directed</b> edge connecting nodes <code>u</code> and <code>v</code>, where <code>u</code> is a parent of child <code>v</code>.
</p><p>
Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.
</p><p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given directed graph will be like this:
  1
 / \
v   v
2-->3
</pre>
</p>
<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4], [4,1], [1,5]]
<b>Output:</b> [4,1]
<b>Explanation:</b> The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
</pre>
</p>
<p><b>Note:</b><br />
<li>The size of the input 2D-array will be between 3 and 1000.</li>
<li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>
</p>

 **difficulty**: Hard

 **topic**: Tree, Depth-first Search, Union Find, Graph, 

