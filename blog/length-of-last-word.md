Leetcode 58. 最后一个单词的长度
<p>给定一个仅包含大小写字母和空格&nbsp;<code>&#39; &#39;</code>&nbsp;的字符串 <code>s</code>，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。</p>


<p>如果不存在最后一个单词，请返回 0&nbsp;。</p>



<p><strong>说明：</strong>一个单词是指仅由字母组成、不包含任何空格字符的 <strong>最大子字符串</strong>。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> &quot;Hello World&quot;

<strong>输出:</strong> 5

</pre>





 **难度**: Easy



 **标签**: 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了96.39% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了73.72% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')   # 去除右侧空格
        words = s.split(' ')    # 以空格划开单词
        return len(words[-1])   # 取最后一个单词的长度
</code></pre></div>
