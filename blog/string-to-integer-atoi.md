Leetcode 8. 字符串转换整数 (atoi)
<p>请你来实现一个&nbsp;<code>atoi</code>&nbsp;函数，使其能将字符串转换成整数。</p>


<p>首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：</p>



<ul>

	<li>如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。</li>

	<li>假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。</li>

	<li>该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。</li>

</ul>



<p>注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。</p>



<p>在任何情况下，若函数不能进行有效的转换时，请返回 0 。</p>



<p><strong>提示：</strong></p>



<ul>

	<li>本题中的空白字符只包括空格字符 <code>&#39; &#39;</code> 。</li>

	<li>假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。如果数值超过这个范围，请返回 &nbsp;INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) 或&nbsp;INT_MIN (&minus;2<sup>31</sup>) 。</li>

</ul>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> &quot;42&quot;

<strong>输出:</strong> 42

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> &quot;   -42&quot;

<strong>输出:</strong> -42

<strong>解释: </strong>第一个非空白字符为 &#39;-&#39;, 它是一个负号。

&nbsp;    我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

</pre>



<p><strong>示例&nbsp;3:</strong></p>



<pre><strong>输入:</strong> &quot;4193 with words&quot;

<strong>输出:</strong> 4193

<strong>解释:</strong> 转换截止于数字 &#39;3&#39; ，因为它的下一个字符不为数字。

</pre>



<p><strong>示例&nbsp;4:</strong></p>



<pre><strong>输入:</strong> &quot;words and 987&quot;

<strong>输出:</strong> 0

<strong>解释:</strong> 第一个非空字符是 &#39;w&#39;, 但它不是数字或正、负号。

     因此无法执行有效的转换。</pre>



<p><strong>示例&nbsp;5:</strong></p>



<pre><strong>输入:</strong> &quot;-91283472332&quot;

<strong>输出:</strong> -2147483648

<strong>解释:</strong> 数字 &quot;-91283472332&quot; 超过 32 位有符号整数范围。 

&nbsp;    因此返回 INT_MIN (&minus;2<sup>31</sup>) 。

</pre>





 **难度**: Medium



 **标签**: 数学、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms
内存消耗：13.6 MB

解题思路：
    这离使用的是官方提供的 自动机 思想。
    首先，分析各字符对应的状态：
                        ' '     +-      numbel      other
            start       start   signed  innumbel    end
            signed      end     end     innumbel    end
            innumbel    end     end     innumbel    end
            end         end     end     end         end
    初始状态为 start,
    在start状态下， 若首字符为' '，则状态不变。若首字符为+-，则将状态调为 signed。 若首字符是数字，则状态调整为 innumbel， 若是其他字符，则调为 end.
    在signed状态下，若字符为数字，则将状态调整为innumbel， 否则为end
    在innumbel状态下，若字符为数字，则保持innumbel状态，否则为end

    具体实现见代码注释
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        am = AM()
        for c in str:
            if am.state == 'end':
                break
            am.get(c)
        return am.sign * am.num


class AM:
    def __init__(self):
        self.tabel = {
            'start': ['start', 'signed', 'innumbel', 'end'],
            'signed': ['end', 'end', 'innumbel', 'end'],
            'innumbel': ['end', 'end', 'innumbel', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }                       # 状态表
        self.sign = 1           # 初始符号为正
        self.num = 0            # 用于存储转换后的数字
        self.state = 'start'    # 初始状态为start
        self.max_ = 2**31 - 1   # 最大数值限制，这里初始限制为 2**31-1 （正数）

    def get_col(self, c:str) -> int:    # 首字符判断，返回为状态表列的索引
        if c.isdigit():
            return 2    # innumbel
        if c.isspace():
            return 0    # start
        if c == '+' or c == '-':
            return 1    # signed
        else:
            return 3    # end

    def get(self, c):
        self.state = self.tabel[self.state][self.get_col(c)]
        if self.state == 'start':   # start 不操作，继续下一个字符
            pass
        if self.state == 'signed':  # signed 将状态调整为signed，且对初始符号与最大数值进行调整
            if c == '+':
                self.sign = 1
            else:
                self.sign = -1
                self.max_ = self.max_ + 1   # 负数时，2**31

        if self.state == 'innumbel':    # innumbel 状态时，计算数值且累加
            self.num = self.num *10 + int(c)
            if self.num > self.max_:    # 若超出数值限制，则将状态置为end
                self.num = self.max_
                self.state = 'end'

        if self.state == 'end':     # end 不做操作
            pass


</code></pre></div>
