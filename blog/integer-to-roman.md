Leetcode 12. 整数转罗马数字
<p>罗马数字包含以下七种字符：&nbsp;<code>I</code>，&nbsp;<code>V</code>，&nbsp;<code>X</code>，&nbsp;<code>L</code>，<code>C</code>，<code>D</code>&nbsp;和&nbsp;<code>M</code>。</p>


<pre><strong>字符</strong>          <strong>数值</strong>

I             1

V             5

X             10

L             50

C             100

D             500

M             1000</pre>



<p>例如， 罗马数字 2 写做&nbsp;<code>II</code>&nbsp;，即为两个并列的 1。12 写做&nbsp;<code>XII</code>&nbsp;，即为&nbsp;<code>X</code>&nbsp;+&nbsp;<code>II</code>&nbsp;。 27 写做&nbsp;&nbsp;<code>XXVII</code>, 即为&nbsp;<code>XX</code>&nbsp;+&nbsp;<code>V</code>&nbsp;+&nbsp;<code>II</code>&nbsp;。</p>



<p>通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做&nbsp;<code>IIII</code>，而是&nbsp;<code>IV</code>。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为&nbsp;<code>IX</code>。这个特殊的规则只适用于以下六种情况：</p>



<ul>

	<li><code>I</code>&nbsp;可以放在&nbsp;<code>V</code>&nbsp;(5) 和&nbsp;<code>X</code>&nbsp;(10) 的左边，来表示 4 和 9。</li>

	<li><code>X</code>&nbsp;可以放在&nbsp;<code>L</code>&nbsp;(50) 和&nbsp;<code>C</code>&nbsp;(100) 的左边，来表示 40 和&nbsp;90。&nbsp;</li>

	<li><code>C</code>&nbsp;可以放在&nbsp;<code>D</code>&nbsp;(500) 和&nbsp;<code>M</code>&nbsp;(1000) 的左边，来表示&nbsp;400 和&nbsp;900。</li>

</ul>



<p>给定一个整数，将其转为罗马数字。输入确保在 1&nbsp;到 3999 的范围内。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong>&nbsp;3

<strong>输出:</strong> &quot;III&quot;</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong>&nbsp;4

<strong>输出:</strong> &quot;IV&quot;</pre>



<p><strong>示例&nbsp;3:</strong></p>



<pre><strong>输入:</strong>&nbsp;9

<strong>输出:</strong> &quot;IX&quot;</pre>



<p><strong>示例&nbsp;4:</strong></p>



<pre><strong>输入:</strong>&nbsp;58

<strong>输出:</strong> &quot;LVIII&quot;

<strong>解释:</strong> L = 50, V = 5, III = 3.

</pre>



<p><strong>示例&nbsp;5:</strong></p>



<pre><strong>输入:</strong>&nbsp;1994

<strong>输出:</strong> &quot;MCMXCIV&quot;

<strong>解释:</strong> M = 1000, CM = 900, XC = 90, IV = 4.</pre>





 **难度**: Medium



 **标签**: 数学、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了93.52% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了79.33% 的用户

解题思路：
    依次取出数字的最后一位进行判断
    罗马数字分几种情况：
        1~3:    III
        4:      IV
        5:      V
        6-8:    VIII
        9:      IX
    用列表分别存储 1 5 10在不同位上的表示，即：[[1, 5, 10], [10, 50, 100], [100, 500, 1000], [1000]]
    在不同位时，用不同位的表示依照罗马数字分情况处理即可
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = [
            ['I', 'V', 'X',],
            ['X', 'L', 'C'],
            ['C', 'D', 'M'],
            ['M']
        ]
        result = ''
        i = 0
        while num:
            roman = roman_list[i]
            num_ = num%10
            if num_ <= 3:
                result = roman[0]*num_ + result
            elif num_ == 4:
                result = roman[0] + roman[1] + result
            elif num_ == 5:
                result = roman[1] + result

            elif 5 < num_ <= 8:
                result = roman[1] + roman[0]*(num_-5) + result

            elif num_ == 9:
                result = roman[0] + roman[2] + result

            i += 1
            num = num // 10
        return result</code></pre></div>
