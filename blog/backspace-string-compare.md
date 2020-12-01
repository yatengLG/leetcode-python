Leetcode 844. 比较含退格的字符串
<p>给定 <code>S</code> 和 <code>T</code> 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 <code>#</code> 代表退格字符。</p>


<p><strong>注意：</strong>如果对空文本输入退格字符，文本继续为空。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>S = &quot;ab#c&quot;, T = &quot;ad#c&quot;

<strong>输出：</strong>true

<strong>解释：</strong>S 和 T 都会变成 &ldquo;ac&rdquo;。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>S = &quot;ab##&quot;, T = &quot;c#d#&quot;

<strong>输出：</strong>true

<strong>解释：</strong>S 和 T 都会变成 &ldquo;&rdquo;。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>S = &quot;a##c&quot;, T = &quot;#a#c&quot;

<strong>输出：</strong>true

<strong>解释：</strong>S 和 T 都会变成 &ldquo;c&rdquo;。

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>S = &quot;a#c&quot;, T = &quot;b&quot;

<strong>输出：</strong>false

<strong>解释：</strong>S 会变成 &ldquo;c&rdquo;，但 T 仍然是 &ldquo;b&rdquo;。</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= S.length &lt;= 200</code></li>

	<li><code>1 &lt;= T.length &lt;= 200</code></li>

	<li><code>S</code> 和 <code>T</code> 只含有小写字母以及字符 <code>&#39;#&#39;</code>。</li>

</ol>



<p>&nbsp;</p>



<p><strong>进阶：</strong></p>



<ul>

	<li>你可以用 <code>O(N)</code> 的时间复杂度和 <code>O(1)</code> 的空间复杂度解决该问题吗？</li>

</ul>



<p>&nbsp;</p>





 **难度**: Easy



 **标签**: 栈、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.39% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.32% 的用户

解题思路：
    栈
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for i in S:
            if i == '#':    # 如果是# ，出栈退格
                if s:
                    s.pop()
            else:           # 字母，进栈
                s.append(i)

        for i in T:
            if i == '#':
                if t:
                    t.pop()
            else:
                t.append(i)
        return s == t
</code></pre></div>
