Leetcode 14. 最长公共前缀
<p>编写一个函数来查找字符串数组中的最长公共前缀。</p>


<p>如果不存在公共前缀，返回空字符串&nbsp;<code>&quot;&quot;</code>。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]

<strong>输出:</strong> &quot;fl&quot;

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]

<strong>输出:</strong> &quot;&quot;

<strong>解释:</strong> 输入不存在公共前缀。

</pre>



<p><strong>说明:</strong></p>



<p>所有输入只包含小写字母&nbsp;<code>a-z</code>&nbsp;。</p>





 **难度**: Easy



 **标签**: 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了35.61% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了33.84% 的用户

解题思路：
    拿第一个字符串去比较其他字符串
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        for string in strs[1:]:
            result_ = ''
            for r,s in zip(result, string):
                if r == s:
                    result_ += r
                else:
                    break
            result = result_

            if result == '':
                break
        return result</code></pre></div>
