Leetcode 面试题 08.07. 无重复字符串的排列组合
<p>无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。</p>


<p> <strong>示例1:</strong></p>



<pre>

<strong> 输入</strong>：S = "qwe"

<strong> 输出</strong>：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

</pre>



<p> <strong>示例2:</strong></p>



<pre>

<strong> 输入</strong>：S = "ab"

<strong> 输出</strong>：["ab", "ba"]

</pre>



<p> <strong>提示:</strong></p>



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
执行用时：288 ms, 在所有 Python3 提交中击败了5.29% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了33.22% 的用户

解题思路：
    回溯
    通过一个列表记录已经使用过的字符下标
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        result = []
        def backtrack(current, used):
            if len(current) >= n:
                result.append(''.join(current[:]))

            for i in range(n):
                if i not in used:
                    backtrack(current+[S[i]], used+[i])
        backtrack([], [])
        return result


"""
执行用时：152 ms, 在所有 Python3 提交中击败了71.82% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了13.36% 的用户

解题思路：
    回溯
    更新当前字符串
"""
class Solution:
    def permutation(self, S: str) -> List[str]:
        result = []
        def backtrack(s, current):  # 当前剩余字符串
            if s == '':
                result.append(current)

            for i in range(len(s)):
                backtrack(s[:i]+s[i+1:], current+s[i])

        backtrack(S, '')
        return result

"""
"""
</code></pre></div>
