Leetcode 118. 杨辉三角
<p>给定一个非负整数&nbsp;<em>numRows，</em>生成杨辉三角的前&nbsp;<em>numRows&nbsp;</em>行。</p>


<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif"></p>



<p><small>在杨辉三角中，每个数是它左上方和右上方的数的和。</small></p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> 5

<strong>输出:</strong>

[

     [1],

    [1,1],

   [1,2,1],

  [1,3,3,1],

 [1,4,6,4,1]

]</pre>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了93.78% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了56.53% 的用户

解题思路：
    模拟杨辉三角的生成过程
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows+1):   # 每一行有i个数
            row = [1]   # 第一个数是1
            for j in range(1, i-1): # 从第二个到倒数第二个起，等于上一行对应数的和
                row.append(result[-1][j-1] + result[-1][j])
            if i > 1:
                row.append(1)
            result.append(row)
        return result
</code></pre></div>
