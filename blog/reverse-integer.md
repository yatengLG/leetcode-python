Leetcode 7. 整数反转
<p>给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> 123

<strong>输出:</strong> 321

</pre>



<p><strong>&nbsp;示例 2:</strong></p>



<pre><strong>输入:</strong> -123

<strong>输出:</strong> -321

</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入:</strong> 120

<strong>输出:</strong> 21

</pre>



<p><strong>注意:</strong></p>



<p>假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。</p>





 **难度**: Easy



 **标签**: 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了44.37% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了75.16% 的用户

解题思路：
    判断输入整数正负并记录，依次取出输入整数的最后一位，存入列表，再反序取出
"""
class Solution:
    def reverse(self, x: int) -> int:

        if x<0:
            negative = -1
            x = -x
            max_ = 2**31
        else:
            max_ = 2**31-1
            negative = 1
        record = []
        print(max_)
        while x != 0:
            record.append(x%10)
            x = x//10

        num = 0
        for i, v in enumerate(record[::-1]):
            num += v*10**i
            if num > max_:
                return 0
        return num*negative
</code></pre></div>
