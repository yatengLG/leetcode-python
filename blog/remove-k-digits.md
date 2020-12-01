Leetcode 402. 移掉K位数字
<p>给定一个以字符串表示的非负整数&nbsp;<em>num</em>，移除这个数中的 <em>k </em>位数字，使得剩下的数字最小。</p>


<p><strong>注意:</strong></p>



<ul>

	<li><em>num</em> 的长度小于 10002 且&nbsp;&ge; <em>k。</em></li>

	<li><em>num</em> 不会包含任何前导零。</li>

</ul>



<p><strong>示例 1 :</strong></p>



<pre>

输入: num = &quot;1432219&quot;, k = 3

输出: &quot;1219&quot;

解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

</pre>



<p><strong>示例 2 :</strong></p>



<pre>

输入: num = &quot;10200&quot;, k = 1

输出: &quot;200&quot;

解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

</pre>



<p>示例<strong> 3 :</strong></p>



<pre>

输入: num = &quot;10&quot;, k = 2

输出: &quot;0&quot;

解释: 从原数字移除所有的数字，剩余为空就是0。

</pre>





 **难度**: Medium



 **标签**: 栈、 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了69.82% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了6.73% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        self.k = k
        def insert(c):  # 插入c字符
            # print(c, self.k, result)
            if result == [] or self.k < 1 or c >= result[-1]:   # 如果result为空，k<1，或者当前c大于栈顶元素， c入栈
                result.append(c)
            else:   # 否则，出栈一个字符，重新尝试插入c
                result.pop()
                self.k -= 1
                insert(c)

        for c in num:   # 一次插入num中数字
            if self.k > 0:
                insert(c)
            else:
                result.append(c)

        for i in range(self.k): # 当k>1时，如果栈不空，则继续出栈
            if result:
                result.pop()
        if result == []:
            result = ['0']
        return str(int(''.join(result)))

</code></pre></div>
