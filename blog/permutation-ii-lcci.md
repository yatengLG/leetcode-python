Leetcode 面试题 08.08. 有重复字符串的排列组合
<p>有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。</p>


<p><strong>示例1:</strong></p>



<pre><strong> 输入</strong>：S = &quot;qqe&quot;

<strong> 输出</strong>：[&quot;eqq&quot;,&quot;qeq&quot;,&quot;qqe&quot;]

</pre>



<p><strong>示例2:</strong></p>



<pre><strong> 输入</strong>：S = &quot;ab&quot;

<strong> 输出</strong>：[&quot;ab&quot;, &quot;ba&quot;]

</pre>



<p><strong>提示:</strong></p>



<ol>

	<li>字符都是英文字母。</li>

	<li>字符串长度在[1, 9]之间。</li>

</ol>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了89.10% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了43.09% 的用户

解题思路：
    回溯
    更新当前剩余字符串，跳过当前字符串中已经处理过的元素
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        result = []
        def backtrack(s, current):  # 当前剩余字符串，当前字符串
            if s == '':
                result.append(current[:])
                return
            for i in range(len(s)):
                if i > 0 and s[i] in s[:i]: # 跳过当前剩余字符串中重复的元素
                    continue
                backtrack(s[:i]+s[i+1:], current+s[i])
        backtrack(S, '')
        return result
</code></pre></div>
