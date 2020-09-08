<h2>93. 复原IP地址</h2><p>给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。</p>

<p><strong>有效的 IP 地址</strong> 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>&#39;.&#39; </code>分隔。</p>

<p>例如：&quot;0.1.2.201&quot; 和 &quot;192.168.1.1&quot; 是 <strong>有效的</strong> IP 地址，但是 &quot;0.011.255.245&quot;、&quot;192.168.1.312&quot; 和 &quot;192.168@1.1&quot; 是 <strong>无效的</strong> IP 地址。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;25525511135&quot;
<strong>输出：</strong>[&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;0000&quot;
<strong>输出：</strong>[&quot;0.0.0.0&quot;]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;1111&quot;
<strong>输出：</strong>[&quot;1.1.1.1&quot;]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;010010&quot;
<strong>输出：</strong>[&quot;0.10.0.10&quot;,&quot;0.100.1.0&quot;]
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;101023&quot;
<strong>输出：</strong>[&quot;1.0.10.23&quot;,&quot;1.0.102.3&quot;,&quot;10.1.0.23&quot;,&quot;10.10.2.3&quot;,&quot;101.0.2.3&quot;]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>


 **难度**: Medium

 **标签**: 字符串、 回溯算法、 


------

<h2>93. Restore IP Addresses</h2><p>Given a string <code>s</code> containing only digits, return all possible valid IP addresses that can be obtained from <code>s</code>. You can return them in <strong>any</strong> order.</p>

<p>A <strong>valid IP address</strong> consists of exactly four integers, each integer is between <code>0</code> and <code>255</code>, separated by single dots and cannot have leading zeros. For example, &quot;0.1.2.201&quot; and &quot;192.168.1.1&quot; are <strong>valid</strong> IP addresses and &quot;0.011.255.245&quot;, &quot;192.168.1.312&quot; and &quot;192.168@1.1&quot; are <strong>invalid</strong> IP addresses.&nbsp;</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "25525511135"
<strong>Output:</strong> ["255.255.11.135","255.255.111.35"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "0000"
<strong>Output:</strong> ["0.0.0.0"]
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "1111"
<strong>Output:</strong> ["1.1.1.1"]
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "010010"
<strong>Output:</strong> ["0.10.0.10","0.100.1.0"]
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> s = "101023"
<strong>Output:</strong> ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3000</code></li>
	<li><code>s</code> consists of digits only.</li>
</ul>


 **difficulty**: Medium

 **topic**: String, Backtracking, 

