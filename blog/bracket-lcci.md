Leetcode 面试题 08.09. 括号
<p>括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。</p>


<p>说明：解集不能包含重复的子集。</p>



<p>例如，给出 n = 3，生成结果为：</p>



<pre>

[

  "((()))",

  "(()())",

  "(())()",

  "()(())",

  "()()()"

]

</pre>





 **难度**: Medium



 **标签**: 字符串、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了85.42% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了29.31% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(l, r, current):   # 剩余左括号个数，剩余右括号个数，当前括号组合
            if l == 0 and r == 0:       # 如果括号都用完，则添加到最终结果中
                result.append(current[:])
                return
            if l > r or l < 0 or r < 0: # 如果剩余左括号比剩余右括号多，或左括号用完，或右括号用完，跳出
                return
            backtrack(l-1, r, current+'(')  # 使用一个左括号
            backtrack(l, r-1, current+')')  # 使用一个右括号
        backtrack(n, n, '')
        return result</code></pre></div>
