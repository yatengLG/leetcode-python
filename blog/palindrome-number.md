Leetcode 9. 回文数
<p>判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> 121

<strong>输出:</strong> true

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> -121

<strong>输出:</strong> false

<strong>解释:</strong> 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入:</strong> 10

<strong>输出:</strong> false

<strong>解释:</strong> 从右向左读, 为 01 。因此它不是一个回文数。

</pre>



<p><strong>进阶:</strong></p>



<p>你能不将整数转为字符串来解决这个问题吗？</p>





 **难度**: Easy



 **标签**: 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了38.64% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了11.30% 的用户

解题思路：
    这里没有将数字转字符串进行判断。
    而是首先对数字进行了判断，限制在一个范围内，然后将数字翻转后进行判断。
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x>2147447412: # 2147447412 是 2*31-1 内最大的回文数。负数 按题意可知均不回文
            return False
        x_copy = x
        num = 0
        while x:                # 翻转数字
            num = num*10 + x%10
            x = x//10
        if num == x_copy:
            return True
        else:
            return False</code></pre></div>
