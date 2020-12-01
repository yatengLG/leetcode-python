Leetcode 6. Z 字形变换
<p>将一个给定字符串根据给定的行数，以从上往下、从左到右进行&nbsp;Z 字形排列。</p>


<p>比如输入字符串为 <code>&quot;LEETCODEISHIRING&quot;</code>&nbsp;行数为 3 时，排列如下：</p>



<pre>L   C   I   R

E T O E S I I G

E   D   H   N

</pre>



<p>之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：<code>&quot;LCIRETOESIIGEDHN&quot;</code>。</p>



<p>请你实现这个将字符串进行指定行数变换的函数：</p>



<pre>string convert(string s, int numRows);</pre>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> s = &quot;LEETCODEISHIRING&quot;, numRows = 3

<strong>输出:</strong> &quot;LCIRETOESIIGEDHN&quot;

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> s = &quot;LEETCODEISHIRING&quot;, numRows =&nbsp;4

<strong>输出:</strong>&nbsp;&quot;LDREOEIIECIHNTSG&quot;

<strong>解释:</strong>



L     D     R

E   O E   I I

E C   I H   N

T     S     G</pre>





 **难度**: Medium



 **标签**: 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了96.88% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.00% 的用户

解题思路：
    模拟Z字形排列过程
    初始化numRows个字符串，分别用做模拟z自行排列的各行
    使用i作为行数的索引，d做为翻转
    最终将各行数据连接在一起
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        record = ["" for _ in range(numRows)]
        i, d = 0, -1
        for c in s:
            if i ==0 or i ==numRows-1:
                d = -d
            record[i] += c
            i += d
        return "".join(record)


"""
执行用时：68 ms, 在所有 Python3 提交中击败了70.05% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了5.00% 的用户

解题思路：
    总结规律，
        总体6行时，每行的数间隔为(10, 0), (8, 2), (6, 4), (4, 6), (2, 8), (0, 10)
        总体5行时，每行的数间隔为(8, 0), (6, 2), (4, 4), (2, 6), (0, 8)
        总体4行时，每行的数间隔为(6, 0), (4, 2), (2, 4), (0, 6)

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        len_s = len(s)
        string = ""
        for i in range(numRows):
            p, q  = numRows*2-2-i*2, i*2
            j = i
            overturn = False
            while j < len_s:
                step = q if overturn else p
                if step != 0:
                    string += s[j]
                j += step
                overturn = not overturn
        return string
</code></pre></div>
