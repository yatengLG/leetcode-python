Leetcode 504. 七进制数
<p>给定一个整数，将其转化为7进制，并以字符串形式输出。</p>


<p><strong>示例 1:</strong></p>



<pre>

<strong>输入:</strong> 100

<strong>输出:</strong> &quot;202&quot;

</pre>



<p><strong>示例 2:</strong></p>



<pre>

<strong>输入:</strong> -7

<strong>输出:</strong> &quot;-10&quot;

</pre>



<p><strong>注意:</strong> 输入范围是&nbsp;[-1e7, 1e7] 。</p>





 **难度**: Easy



 **标签**: 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.29% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.15% 的用户

解题思路：
    首先记录符号。
    转七进制，数字除以7取余数，作为当前位的值，并将数字更新为除以7后的值
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = '' # 用于保存结果
        symbol = '' # 记录符号
        if num < 0:
            num = -num
            symbol = '-'
        while num > 6:
            result = str(num%7) + result    # 取除以7后的余数作为当前位的值
            num = num//7    # 更新数字
        result = str(num) + result
        result = symbol + result    # 添加符号
        return result
</code></pre></div>
