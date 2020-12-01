Leetcode 1291. 顺次数
<p>我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 <code>1</code> 的整数。</p>


<p>请你返回由&nbsp;<code>[low, high]</code>&nbsp;范围内所有顺次数组成的 <strong>有序</strong> 列表（从小到大排序）。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输出：</strong>low = 100, high = 300

<strong>输出：</strong>[123,234]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输出：</strong>low = 1000, high = 13000

<strong>输出：</strong>[1234,2345,3456,4567,5678,6789,12345]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>

</ul>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：20 ms, 在所有 Python3 提交中击败了98.96% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了73.87% 的用户

解题思路：
    回溯
    一次以1~9开头，查看符合要求的数字
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        def backtract(now, current):    # 以now开头， current记录当前数字
            if low <= current <= high:  # 符合题意，添加到最终结果
                result.append(current)
            if now >= 9 or current > high:
                return
            backtract(now+1, current*10+now+1)

        for i in range(1, 10):  # 以1~9依次作为开头
            backtract(i, i)
        result.sort()
        return result</code></pre></div>
