Leetcode 459. 重复的子字符串
<p>给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。</p>


<p><strong>示例 1:</strong></p>



<pre>

<strong>输入:</strong> &quot;abab&quot;



<strong>输出:</strong> True



<strong>解释:</strong> 可由子字符串 &quot;ab&quot; 重复两次构成。

</pre>



<p><strong>示例 2:</strong></p>



<pre>

<strong>输入:</strong> &quot;aba&quot;



<strong>输出:</strong> False

</pre>



<p><strong>示例 3:</strong></p>



<pre>

<strong>输入:</strong> &quot;abcabcabcabc&quot;



<strong>输出:</strong> True



<strong>解释:</strong> 可由子字符串 &quot;abc&quot; 重复四次构成。 (或者子字符串 &quot;abcabc&quot; 重复两次构成。)

</pre>





 **难度**: Easy



 **标签**: 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了63.18% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了96.94% 的用户

解题思路：
    暴力解法。

"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2+1):  # 首先根据字符串长度判断可以被分为几段
            if n%i == 0:
                if s[:i] * (n//i) == s: # 判断字符串是否可以由当前分段组成
                    return True
        return False
</code></pre></div>
