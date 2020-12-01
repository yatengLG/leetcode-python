Leetcode 3. 无重复字符的最长子串
<p>给定一个字符串，请你找出其中不含有重复字符的&nbsp;<strong>最长子串&nbsp;</strong>的长度。</p>


<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入: </strong>&quot;abcabcbb&quot;

<strong>输出: </strong>3 

<strong>解释:</strong> 因为无重复字符的最长子串是 <code>&quot;abc&quot;，所以其</code>长度为 3。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入: </strong>&quot;bbbbb&quot;

<strong>输出: </strong>1

<strong>解释: </strong>因为无重复字符的最长子串是 <code>&quot;b&quot;</code>，所以其长度为 1。

</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入: </strong>&quot;pwwkew&quot;

<strong>输出: </strong>3

<strong>解释: </strong>因为无重复字符的最长子串是&nbsp;<code>&quot;wke&quot;</code>，所以其长度为 3。

&nbsp;    请注意，你的答案必须是 <strong>子串 </strong>的长度，<code>&quot;pwke&quot;</code>&nbsp;是一个<em>子序列，</em>不是子串。

</pre>





 **难度**: Medium



 **标签**: 哈希表、 双指针、 字符串、 None、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：72 ms, 在所有 Python3 提交中击败了82.59% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.88%

解题思路：
    双指针，一个遍历字符串，一个记录当前子串起始点。
    使用字典存放字符串元素，
    若元素重复：
        更新子串起始点
        字典更新元素下标
        计算最大子串长度
    若不重复：
        字典登记元素，记录下标
        更新最大子串长度
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_, max_ = -1, 0
        record = {}
        for i, v in enumerate(s):
            if v not in record:
                record[v] = i
                max_ = max(i - start_, max_)
            else:
                start_ = max(record[v], start_)
                record[v] = i
                max_ = max(i - start_, max_)
        return max_



</code></pre></div>
