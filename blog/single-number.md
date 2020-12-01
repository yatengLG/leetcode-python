Leetcode 136. 只出现一次的数字
<p>给定一个<strong>非空</strong>整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。</p>


<p><strong>说明：</strong></p>



<p>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> [2,2,1]

<strong>输出:</strong> 1

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> [4,1,2,1,2]

<strong>输出:</strong> 4</pre>





 **难度**: Easy



 **标签**: 位运算、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了31.59% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.69% 的用户

解题思路：
    位运算-异或
    a ^ 0 = a
    a ^ a = 0
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)</code></pre></div>
