Leetcode 925. 长按键入
<p>你的朋友正在使用键盘输入他的名字&nbsp;<code>name</code>。偶尔，在键入字符&nbsp;<code>c</code>&nbsp;时，按键可能会被<em>长按</em>，而字符可能被输入 1 次或多次。</p>


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





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了81.82% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了18.18% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p, q = 0, 0     #指针
        while p < len(name) and q < len(typed):
            if name[p] == typed[q]: # 如果对应位置匹配，指针同时后移，匹配下一个
                p += 1
                q += 1
            else:
                if q > 0 and typed[q-1] == typed[q]:    # 如果typed存在连击，匹配下一个
                    q += 1
                else:   # 不存在连击，返回False
                    return False
        if p >= len(name):   # name匹配完
            if q >= len(typed):  # typed 也匹配完
                return True
            else:
                while q < len(typed):   # 若typed没有匹配完，且后续连击，返回True
                    if typed[q] != typed[q-1]:  # 若不存在连击，则返回False
                        return False
                    q += 1
                return True
        else:
            return False
</code></pre></div>
