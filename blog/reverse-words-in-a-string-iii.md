Leetcode 557. 反转字符串中的单词 III
<p>给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。</p>


<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>&quot;Let&#39;s take LeetCode contest&quot;

<strong>输出：</strong>&quot;s&#39;teL ekat edoCteeL tsetnoc&quot;

</pre>



<p>&nbsp;</p>



<p><strong><strong><strong><strong>提示：</strong></strong></strong></strong></p>



<ul>

	<li>在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。</li>

</ul>





 **难度**: Easy



 **标签**: 字符串、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了96.66% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了76.81% 的用户

解题思路：
    先将字符串按空格划分， 然后把每部分翻转，然后在每部分中间添加空格构成字符串
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')   # 以空格划分
        for i in range(len(ss)):
            ss[i] = ss[i][::-1] # 翻转每一部分
        return ' '.join(ss) # 添加空格
</code></pre></div>
