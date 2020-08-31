<h2>368. 最大整除子集</h2><p>给出一个由<strong>无重复的</strong>正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (S<sub>i，</sub>S<sub>j</sub>) 都要满足：S<sub>i</sub> % S<sub>j</sub> = 0 或 S<sub>j</sub> % S<sub>i</sub> = 0。</p>

<p>如果有多个目标子集，返回其中任何一个均可。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [1,2,3]
<strong>输出:</strong> [1,2] (当然, [1,3] 也正确)
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [1,2,4,8]
<strong>输出:</strong> [1,2,4,8]
</pre>


 **难度**: Medium

 **标签**: 数学、 动态规划、 


------

<h2>368. Largest Divisible Subset</h2><p>Given a set of <b>distinct</b> positive integers, find the largest subset such that every pair (S<sub>i</sub>, S<sub>j</sub>) of elements in this subset satisfies:</p>

<p>S<sub>i</sub> % S<sub>j</sub> = 0 or S<sub>j</sub> % S<sub>i</sub> = 0.</p>

<p>If there are multiple solutions, return any subset is fine.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-1">[1,2] </span>(of course, [1,3] will also be ok)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,4,8]</span>
<strong>Output: </strong><span id="example-output-2">[1,2,4,8]</span>
</pre>
</div>
</div>

 **difficulty**: Medium

 **topic**: Math, Dynamic Programming, 

