Leetcode 204. 计数质数
<p>统计所有小于非负整数&nbsp;<em><code>n</code>&nbsp;</em>的质数的数量。</p>


<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>n = 10

<strong>输出：</strong>4

<strong>解释：</strong>小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>n = 0

<strong>输出：</strong>0

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>n = 1

<strong>输出</strong>：0

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>

</ul>





 **难度**: Easy



 **标签**: 哈希表、 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了95.17% 的用户
内存消耗：36.3 MB, 在所有 Python3 提交中击败了6.94% 的用户

解题思路：
    厄拉多塞筛法
    https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:   # 1, 2 不存在质数
            return 0
        record = [1] * n    # 记录质数，record[i]=1 表示， i+1是质数
        record[0], record[1] = 0, 0  # 1, 2不是质数
        for i in range(2, int(n**0.5)+1):
            if record[i]:
                record[i*i:n:i] = [0]*((n-1-i*i)//i+1)  # 如果当前i是质数，则2*i， 3*i ... 均不是质数
        return sum(record)


</code></pre></div>
