Leetcode 150. 逆波兰表达式求值
<p>根据<a href="https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437" target="_blank"> 逆波兰表示法</a>，求表达式的值。</p>


<p>有效的运算符包括&nbsp;<code>+</code>,&nbsp;<code>-</code>,&nbsp;<code>*</code>,&nbsp;<code>/</code>&nbsp;。每个运算对象可以是整数，也可以是另一个逆波兰表达式。</p>



<p>&nbsp;</p>



<p><strong>说明：</strong></p>



<ul>

	<li>整数除法只保留整数部分。</li>

	<li>给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。</li>

</ul>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1：</strong></p>



<pre><strong>输入:</strong> [&quot;2&quot;, &quot;1&quot;, &quot;+&quot;, &quot;3&quot;, &quot;*&quot;]

<strong>输出:</strong> 9

<strong>解释:</strong> 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入:</strong> [&quot;4&quot;, &quot;13&quot;, &quot;5&quot;, &quot;/&quot;, &quot;+&quot;]

<strong>输出:</strong> 6

<strong>解释:</strong> 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

</pre>



<p><strong>示例&nbsp;3：</strong></p>



<pre><strong>输入:</strong> [&quot;10&quot;, &quot;6&quot;, &quot;9&quot;, &quot;3&quot;, &quot;+&quot;, &quot;-11&quot;, &quot;*&quot;, &quot;/&quot;, &quot;*&quot;, &quot;17&quot;, &quot;+&quot;, &quot;5&quot;, &quot;+&quot;]

<strong>输出:</strong> 22

<strong>解释:</strong> 

该算式转化为常见的中缀算术表达式为：

  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5

= ((10 * (6 / (12 * -11))) + 17) + 5

= ((10 * (6 / -132)) + 17) + 5

= ((10 * 0) + 17) + 5

= (0 + 17) + 5

= 17 + 5

= 22</pre>



<p>&nbsp;</p>



<p><strong>逆波兰表达式：</strong></p>



<p>逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。</p>



<ul>

	<li>平常使用的算式则是一种中缀表达式，如 <code>( 1 + 2 ) * ( 3 + 4 )</code> 。</li>

	<li>该算式的逆波兰表达式写法为 <code>( ( 1 2 + ) ( 3 4 + ) * )</code> 。</li>

</ul>



<p>逆波兰表达式主要有以下两个优点：</p>



<ul>

	<li>去掉括号后表达式无歧义，上式即便写成 <code>1 2 + 3 4 + * </code>也可以依据次序计算出正确结果。</li>

	<li>适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。</li>

</ul>





 **难度**: Medium



 **标签**: 栈、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.20% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.27% 的用户

解题思路：
    栈
    当遇到+-*/时，出栈两个，进行计算后，将结果入栈
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []
        for token in tokens:
            if token == '+':
                b = record.pop()    # 出栈两个数字，分别作为a,b
                a = record.pop()
                cal = int(int(a) + int(b))  # 计算获得结果，并将计算结果入栈
                record.append(cal)
            elif token == '-':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) - int(b))
                record.append(cal)
            elif token == '*':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) * int(b))
                record.append(cal)
            elif token == '/':
                b = record.pop()
                a = record.pop()
                cal = int(int(a) / int(b))
                record.append(cal)
            else:
                record.append(token)
        return int(record.pop())</code></pre></div>
