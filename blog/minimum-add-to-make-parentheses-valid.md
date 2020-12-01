Leetcode 921. 使括号有效的最少添加
<p>给定一个由&nbsp;<code>&#39;(&#39;</code>&nbsp;和&nbsp;<code>&#39;)&#39;</code>&nbsp;括号组成的字符串 <code>S</code>，我们需要添加最少的括号（ <code>&#39;(&#39;</code>&nbsp;或是&nbsp;<code>&#39;)&#39;</code>，可以在任何位置），以使得到的括号字符串有效。</p>


<p>从形式上讲，只有满足下面几点之一，括号字符串才是有效的：</p>



<ul>

	<li>它是一个空字符串，或者</li>

	<li>它可以被写成&nbsp;<code>AB</code>&nbsp;（<code>A</code>&nbsp;与&nbsp;<code>B</code>&nbsp;连接）, 其中&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是有效字符串，或者</li>

	<li>它可以被写作&nbsp;<code>(A)</code>，其中&nbsp;<code>A</code>&nbsp;是有效字符串。</li>

</ul>



<p>给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>&quot;())&quot;

<strong>输出：</strong>1

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>&quot;(((&quot;

<strong>输出：</strong>3

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>&quot;()&quot;

<strong>输出：</strong>0

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>&quot;()))((&quot;

<strong>输出：</strong>4</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>S.length &lt;= 1000</code></li>

	<li><code>S</code> 只包含&nbsp;<code>&#39;(&#39;</code> 和&nbsp;<code>&#39;)&#39;</code>&nbsp;字符。</li>

</ol>



<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 栈、 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.66% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.64% 的用户

解题思路：
    统计未匹配的左右括号。
    具体实现见代码注释
"""
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        l, r = 0, 0     # 左括号，右括号未匹配数统计
        for s in S:
            if s == '(':    # 如果是左括号，则左括号+1
                l += 1
            if s == ')':    #
                if l < 1:   # 左括号匹配完后，未匹配的右括号+1
                    r += 1
                else:
                    l -= 1  # 如果有多余的左括号, 则消耗一个左括号
        return l+r  # 返回未匹配的左括号和右括号的总和
</code></pre></div>
