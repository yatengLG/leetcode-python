Leetcode 306. 累加数
<p>累加数是一个字符串，组成它的数字可以形成累加序列。</p>


<p>一个有效的累加序列必须<strong>至少</strong>包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。</p>



<p>给定一个只包含数字&nbsp;<code>&#39;0&#39;-&#39;9&#39;</code>&nbsp;的字符串，编写一个算法来判断给定输入是否是累加数。</p>



<p><strong>说明:&nbsp;</strong>累加序列里的数不会以 0 开头，所以不会出现&nbsp;<code>1, 2, 03</code> 或者&nbsp;<code>1, 02, 3</code>&nbsp;的情况。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> <code>&quot;112358&quot;</code>

<strong>输出:</strong> true 

<strong>解释: </strong>累加序列为: <code>1, 1, 2, 3, 5, 8 </code>。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> <code>&quot;199100199&quot;</code>

<strong>输出:</strong> true 

<strong>解释: </strong>累加序列为: <code>1, 99, 100, 199。</code>1 + 99 = 100, 99 + 100 = 199</pre>



<p><strong>进阶:</strong><br>

你如何处理一个溢出的过大的整数输入?</p>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了65.97% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了54.62% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def backtrack(num, current):
            # print(num, current)
            if num == '' and len(current) > 2:  # 如果当前划分大于2，且字符串均处理完成，则返回True
                return True
            if num == '':   # 如果字符串均处理完，则跳出
                return
            for i in range(1, n):
                if (num[0] == '0' and i < 2) or num[0]!='0':    # 针对以0开头的数字处理，如02 03
                    if len(current)<2 or (len(current) >= 2 and int(num[:i])==int(current[-1])+int(current[-2])):   # 如当前数字个数小于2，则直接添加。如大于2，则需判别是否和等于前两个数想加
                        current.append(num[:i])
                        new_num = num[i:]
                        if backtrack(new_num, current): # 在剩余字符串中寻找下一个数字
                            return True
                        current.pop()   # 回溯

        return backtrack(num, [])

</code></pre></div>
