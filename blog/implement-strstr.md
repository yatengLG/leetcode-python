Leetcode 28. 实现 strStr()
<p>实现&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strStr()</a>&nbsp;函数。</p>


<p>给定一个&nbsp;haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回&nbsp; <strong>-1</strong>。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> haystack = &quot;hello&quot;, needle = &quot;ll&quot;

<strong>输出:</strong> 2

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> haystack = &quot;aaaaa&quot;, needle = &quot;bba&quot;

<strong>输出:</strong> -1

</pre>



<p><strong>说明:</strong></p>



<p>当&nbsp;<code>needle</code>&nbsp;是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。</p>



<p>对于本题而言，当&nbsp;<code>needle</code>&nbsp;是空字符串时我们应当返回 0 。这与C语言的&nbsp;<a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strstr()</a>&nbsp;以及 Java的&nbsp;<a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a>&nbsp;定义相符。</p>





 **难度**: Easy



 **标签**: 双指针、 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG
"""
执行用时：40 ms, 在所有 Python3 提交中击败了80.24% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了97.09% 的用户

解题思路：
    使用双指针分别指向两字符串
    具体实现见代码注释
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        len_i, len_j = len(haystack), len(needle)
        record = -1         # 初始化为-1， 用于记录字符相等时的下标
        i, j = 0, 0         # 双指针
        while i < len_i:    # 循环遍历字符串haystack
            if haystack[i] == needle[j]:    # 若haystack当前下标i指向的字符与needle字符串当前下标j所指向的字符相等
                record = i  # record记录当前i下标
                j += 1      # 后移needle字符串下标
            else:
                i = i-j     # 否则，将i下标移动到之前开始匹配的后一项
                j = 0       # j指针指向needle第一个字符
                record = -1 # record归-1
            if j > len_j-1: # 如needle字符串遍历完毕，则跳出循环
                break
            else:
                record = -1
            i += 1
        if record > 0:  # 匹配成功时，record指向匹配字符串的末尾，需要移动到匹配字符串的开始
            record -= len_j-1
        return record</code></pre></div>
