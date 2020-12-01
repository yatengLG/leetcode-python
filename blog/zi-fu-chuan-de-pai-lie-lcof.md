Leetcode 剑指 Offer 38. 字符串的排列
<p>输入一个字符串，打印出该字符串中字符的所有排列。</p>


<p>&nbsp;</p>



<p>你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre><strong>输入：</strong>s = &quot;abc&quot;

<strong>输出：[</strong>&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;<strong>]</strong>

</pre>



<p>&nbsp;</p>



<p><strong>限制：</strong></p>



<p><code>1 &lt;= s 的长度 &lt;= 8</code></p>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：220 ms, 在所有 Python3 提交中击败了34.50% 的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了49.56% 的用户

解题思路：
    回溯。将字符串转为列表，排序后，跳过重复元素
"""
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        s = list(s)
        s.sort()
        result = []
        def backtrack(current, used):
            if len(current) >= n:
                result.append(''.join(current[:]))
                return
            for i in range(n):
                if i not in used:
                    if i>0 and s[i] == s[i-1] and i-1 not in used:
                        continue
                    backtrack(current+[s[i]], used+[i])

        backtrack([], [])
        return result

"""
执行用时：176 ms, 在所有 Python3 提交中击败了54.66% 的用户
内存消耗：18.3 MB, 在所有 Python3 提交中击败了81.43% 的用户

解题思路：
    回溯
"""
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        result = []

        def backtrack(s, current):  # 剩余字符串， 当前元素
            if len(current) >= n:
                result.append(''.join(current[:]))
                return
            for i in range(len(s)):
                if s[i] in s[:i]:   #跳过当前字符串的重复元素
                    continue
                backtrack(s[:i]+s[i+1:], current+[s[i]])
        backtrack(s, [])
        return result
</code></pre></div>
