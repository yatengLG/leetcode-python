Leetcode 43. 字符串相乘
<p>给定两个以字符串形式表示的非负整数&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>，返回&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的乘积，它们的乘积也表示为字符串形式。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;

<strong>输出:</strong> &quot;6&quot;</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;

<strong>输出:</strong> &quot;56088&quot;</pre>



<p><strong>说明：</strong></p>



<ol>

	<li><code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的长度小于110。</li>

	<li><code>num1</code> 和&nbsp;<code>num2</code> 只包含数字&nbsp;<code>0-9</code>。</li>

	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;均不以零开头，除非是数字 0 本身。</li>

	<li><strong>不能使用任何标准库的大数类型（比如 BigInteger）</strong>或<strong>直接将输入转换为整数来处理</strong>。</li>

</ol>





 **难度**: Medium



 **标签**: 数学、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：244 ms, 在所有 Python3 提交中击败了28.18% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了13.10% 的用户

解题思路：
    模拟竖式乘法运算，逻辑与列竖式相同
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i, val1 in enumerate(num1[::-1]):
            for j, val2 in enumerate(num2[::-1]):
                result += int(val1) * int(val2) * 10 ** (i + j)
        return str(result)

"""
执行用时：124 ms, 在所有 Python3 提交中击败了60.60% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了17.70% 的用户

解题思路：
    优化后，速度大幅提升，使用数组存储每次的计算结构，然后求和    
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        record = [0]*(len(num1)+len(num2))
        for i, val1 in enumerate(num1[::-1]):
            for j, val2 in enumerate(num2[::-1]):
                record[i+j] += int(val1) * int(val2)

        result = 0
        for power, val in enumerate(record):
            result += val*10**power

        return str(result)
</code></pre></div>
