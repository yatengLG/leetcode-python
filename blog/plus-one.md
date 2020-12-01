Leetcode 66. 加一
<p>给定一个由<strong>整数</strong>组成的<strong>非空</strong>数组所表示的非负整数，在该数的基础上加一。</p>


<p>最高位数字存放在数组的首位， 数组中每个元素只存储<strong>单个</strong>数字。</p>



<p>你可以假设除了整数 0 之外，这个整数不会以零开头。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> [1,2,3]

<strong>输出:</strong> [1,2,4]

<strong>解释:</strong> 输入数组表示数字 123。

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> [4,3,2,1]

<strong>输出:</strong> [4,3,2,2]

<strong>解释:</strong> 输入数组表示数字 4321。

</pre>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了88.95% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了48.64% 的用户

解题思路：
    按照题意，模拟数字加1
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1 # 先要加的1，以及记录进位
        index = len(digits)-1
        while index > -1:   # 从最后一位开始计算
            num = digits[index] + add   # 当前位加上进位
            add = num//10       # 更新进位
            digits[index] = num % 10    # 更新当前值
            index -= 1  # 处理下一个
        if add > 0:
            digits.insert(0, add)   # 如果最终进位不为0，则在最开始添加一位
        return digits
</code></pre></div>
