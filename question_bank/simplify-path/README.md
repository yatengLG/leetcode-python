<h2>71. 简化路径</h2><p>以 Unix 风格给出一个文件的<strong>绝对路径</strong>，你需要简化它。或者换句话说，将其转换为规范路径。</p>

<p>在 Unix 风格的文件系统中，一个点（<code>.</code>）表示当前目录本身；此外，两个点 （<code>..</code>）&nbsp;表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：<a href="https://blog.csdn.net/u011327334/article/details/50355600" target="_blank">Linux / Unix中的绝对路径 vs 相对路径</a></p>

<p>请注意，返回的规范路径必须始终以斜杠 <code>/</code> 开头，并且两个目录名之间必须只有一个斜杠 <code>/</code>。最后一个目录名（如果存在）<strong>不能</strong>以 <code>/</code> 结尾。此外，规范路径必须是表示绝对路径的<strong>最短</strong>字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：&quot;</strong>/home/&quot;
<strong>输出：&quot;</strong>/home&quot;
<strong>解释：</strong>注意，最后一个目录名后面没有斜杠。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：&quot;</strong>/../&quot;
<strong>输出：&quot;</strong>/&quot;
<strong>解释：</strong>从根目录向上一级是不可行的，因为根是你可以到达的最高级。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：&quot;</strong>/home//foo/&quot;
<strong>输出：&quot;</strong>/home/foo&quot;
<strong>解释：</strong>在规范路径中，多个连续斜杠需要用一个斜杠替换。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：&quot;</strong>/a/./b/../../c/&quot;
<strong>输出：&quot;</strong>/c&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：&quot;</strong>/a/../../b/../c//.//&quot;
<strong>输出：&quot;</strong>/c&quot;
</pre>

<p><strong>示例 6：</strong></p>

<pre><strong>输入：&quot;</strong>/a//b////c/d//././/..&quot;
<strong>输出：&quot;</strong>/a/b/c&quot;</pre>


 **难度**: Medium

 **标签**: 栈、 字符串、 


------

<h2>71. Simplify Path</h2><p>Given an <strong>absolute path</strong> for a file (Unix-style), simplify it. Or in other words, convert it to the <strong>canonical path</strong>.</p>

<p>In a UNIX-style file system, a period <code>.</code>&nbsp;refers to the current directory. Furthermore, a double period <code>..</code>&nbsp;moves the directory up a level.</p>

<p>Note that the returned canonical path must always begin&nbsp;with a slash <code>/</code>, and there must be only a single slash <code>/</code>&nbsp;between two directory names.&nbsp;The last directory name (if it exists) <b>must not</b>&nbsp;end with a trailing <code>/</code>. Also, the canonical path must be the <strong>shortest</strong> string&nbsp;representing the absolute path.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/home/&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/home&quot;
<strong>Explanation:</strong> Note that there is no trailing slash after the last directory name.</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/../&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/&quot;</span>
<strong>Explanation:</strong> Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/home//foo/&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/home/foo&quot;</span>
<strong>Explanation: </strong>In the canonical path, multiple consecutive slashes are replaced by a single one.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/a/./b/../../c/&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/c&quot;</span>
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/a/../../b/../c//.//&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/c&quot;</span>
</pre>

<p><strong>Example 6:</strong></p>

<pre>
<strong>Input: &quot;</strong><span id="example-input-1-1">/a//b////c/d//././/..&quot;</span>
<strong>Output: &quot;</strong><span id="example-output-1">/a/b/c&quot;</span>
</pre>


 **difficulty**: Medium

 **topic**: Stack, String, 

