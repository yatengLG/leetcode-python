Leetcode 20. 有效的括号
<p>给定一个只包括 <code>&#39;(&#39;</code>，<code>&#39;)&#39;</code>，<code>&#39;{&#39;</code>，<code>&#39;}&#39;</code>，<code>&#39;[&#39;</code>，<code>&#39;]&#39;</code>&nbsp;的字符串，判断字符串是否有效。</p>


<p>有效字符串需满足：</p>



<ol>

	<li>左括号必须用相同类型的右括号闭合。</li>

	<li>左括号必须以正确的顺序闭合。</li>

</ol>



<p>注意空字符串可被认为是有效字符串。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> &quot;()&quot;

<strong>输出:</strong> true

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> &quot;()[]{}&quot;

<strong>输出:</strong> true

</pre>



<p><strong>示例&nbsp;3:</strong></p>



<pre><strong>输入:</strong> &quot;(]&quot;

<strong>输出:</strong> false

</pre>



<p><strong>示例&nbsp;4:</strong></p>



<pre><strong>输入:</strong> &quot;([)]&quot;

<strong>输出:</strong> false

</pre>



<p><strong>示例&nbsp;5:</strong></p>



<pre><strong>输入:</strong> &quot;{[]}&quot;

<strong>输出:</strong> true</pre>





 **难度**: Easy



 **标签**: 栈、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了77.59% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了62.39% 的用户

解题思路：
    栈，使用列表模拟进栈出栈操作
"""

class Solution:
    def isValid(self, s: str) -> bool:
        l_r = {'(': ')', '{': '}', '[': ']'}
        record = []
        for c in s:
            if c == ' ':
                continue
            if c == '(':
                record.append('(')
            elif c == '[':
                record.append('[')
            elif c == '{':
                record.append('{')
            else:
                if record:
                    r_ = record.pop()
                    if l_r[r_] != c:
                        print(r_, '==', c)
                        return False
                else:
                    return False
        if record == []:
            return True
        else:
            return False
</code></pre></div>
