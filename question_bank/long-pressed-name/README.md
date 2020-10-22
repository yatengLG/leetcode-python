<h2>925. 长按键入</h2><p>你的朋友正在使用键盘输入他的名字&nbsp;<code>name</code>。偶尔，在键入字符&nbsp;<code>c</code>&nbsp;时，按键可能会被<em>长按</em>，而字符可能被输入 1 次或多次。</p>

<p>你将会检查键盘输入的字符&nbsp;<code>typed</code>。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回&nbsp;<code>True</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>name = &quot;alex&quot;, typed = &quot;aaleex&quot;
<strong>输出：</strong>true
<strong>解释：</strong>&#39;alex&#39; 中的 &#39;a&#39; 和 &#39;e&#39; 被长按。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
<strong>输出：</strong>false
<strong>解释：</strong>&#39;e&#39; 一定需要被键入两次，但在 typed 的输出中不是这样。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>name = &quot;leelee&quot;, typed = &quot;lleeelee&quot;
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>name = &quot;laiden&quot;, typed = &quot;laiden&quot;
<strong>输出：</strong>true
<strong>解释：</strong>长按名字中的字符并不是必要的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>name.length &lt;= 1000</code></li>
	<li><code>typed.length &lt;= 1000</code></li>
	<li><code>name</code> 和&nbsp;<code>typed</code>&nbsp;的字符都是小写字母。</li>
</ol>

<p>&nbsp;</p>

<p>&nbsp;</p>


 **难度**: Easy

 **标签**: 双指针、 字符串、 


------

<h2>925. Long Pressed Name</h2><p>Your friend is typing his <code>name</code>&nbsp;into a keyboard.&nbsp; Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>

<p>You examine the <code>typed</code>&nbsp;characters of the keyboard.&nbsp; Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;alex&quot;, typed = &quot;aaleex&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>&#39;a&#39; and &#39;e&#39; in &#39;alex&#39; were long pressed.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;saeed&quot;, typed = &quot;ssaaedd&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>&#39;e&#39; must have been pressed twice, but it wasn&#39;t in the typed output.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;leelee&quot;, typed = &quot;lleeelee&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> name = &quot;laiden&quot;, typed = &quot;laiden&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>It&#39;s not necessary to long press any character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= name.length &lt;= 1000</code></li>
	<li><code>1 &lt;= typed.length &lt;= 1000</code></li>
	<li>The characters of <code>name</code> and <code>typed</code> are lowercase letters.</li>
</ul>


 **difficulty**: Easy

 **topic**: Two Pointers, String, 

