<h2>402. 移掉K位数字</h2><p>给定一个以字符串表示的非负整数&nbsp;<em>num</em>，移除这个数中的 <em>k </em>位数字，使得剩下的数字最小。</p>

<p><strong>注意:</strong></p>

<ul>
	<li><em>num</em> 的长度小于 10002 且&nbsp;&ge; <em>k。</em></li>
	<li><em>num</em> 不会包含任何前导零。</li>
</ul>

<p><strong>示例 1 :</strong></p>

<pre>
输入: num = &quot;1432219&quot;, k = 3
输出: &quot;1219&quot;
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
</pre>

<p><strong>示例 2 :</strong></p>

<pre>
输入: num = &quot;10200&quot;, k = 1
输出: &quot;200&quot;
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
</pre>

<p>示例<strong> 3 :</strong></p>

<pre>
输入: num = &quot;10&quot;, k = 2
输出: &quot;0&quot;
解释: 从原数字移除所有的数字，剩余为空就是0。
</pre>


 **难度**: Medium

 **标签**: 栈、 贪心算法、 


------

<h2>402. Remove K Digits</h2><p>Given a non-negative integer <i>num</i> represented as a string, remove <i>k</i> digits from the number so that the new number is the smallest possible.
</p>

<p><b>Note:</b><br />
<ul>
<li>The length of <i>num</i> is less than 10002 and will be &ge; <i>k</i>.</li>
<li>The given <i>num</i> does not contain any leading zero.</li>
</ul>
</b>
</p>

<p><b>Example 1:</b>
<pre>
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
</pre>
</p>

<p><b>Example 3:</b>
<pre>
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
</pre>
</p>

 **difficulty**: Medium

 **topic**: Stack, Greedy, 

