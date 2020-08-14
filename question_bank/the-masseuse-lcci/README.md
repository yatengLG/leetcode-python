<h2>面试题 17.16. 按摩师</h2><p>一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。</p>

<p><strong>注意：</strong>本题相对原题稍作改动</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> [1,2,3,1]
<strong>输出：</strong> 4
<strong>解释：</strong> 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> [2,7,9,3,1]
<strong>输出：</strong> 12
<strong>解释：</strong> 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong> [2,1,4,5,3,1,1,3]
<strong>输出：</strong> 12
<strong>解释：</strong> 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
</pre>


 **难度**: Easy

 **标签**: 动态规划、 


------

<h2>面试题 17.16. The Masseuse LCCI</h2><p>A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to accept. She needs a break between appointments and therefore she cannot accept any adjacent requests. Given a sequence of back-to-back appoint&shy; ment requests, find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes.</p>

<p><b>Note:&nbsp;</b>This problem is slightly different from the original one in the book.</p>

<p>&nbsp;</p>

<p><strong>Example 1: </strong></p>

<pre>
<strong>Input: </strong> [1,2,3,1]
<strong>Output: </strong> 4
<strong>Explanation: </strong> Accept request 1 and 3, total minutes = 1 + 3 = 4
</pre>

<p><strong>Example 2: </strong></p>

<pre>
<strong>Input: </strong> [2,7,9,3,1]
<strong>Output: </strong> 12
<strong>Explanation: </strong> Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
</pre>

<p><strong>Example 3: </strong></p>

<pre>
<strong>Input: </strong> [2,1,4,5,3,1,1,3]
<strong>Output: </strong> 12
<strong>Explanation: </strong> Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12
</pre>


 **difficulty**: Easy

 **topic**: Dynamic Programming, 

