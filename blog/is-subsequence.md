Leetcode 392. 判断子序列
<p>给定字符串 <strong>s</strong> 和 <strong>t</strong> ，判断 <strong>s</strong> 是否为 <strong>t</strong> 的子序列。</p>


<p>你可以认为 <strong>s</strong> 和 <strong>t</strong> 中仅包含英文小写字母。字符串 <strong>t</strong> 可能会很长（长度 ~= 500,000），而 <strong>s</strong> 是个短字符串（长度 &lt;=100）。</p>



<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，<code>&quot;ace&quot;</code>是<code>&quot;abcde&quot;</code>的一个子序列，而<code>&quot;aec&quot;</code>不是）。</p>



<p><strong>示例&nbsp;1:</strong><br />

<strong>s</strong> = <code>&quot;abc&quot;</code>, <strong>t</strong> = <code>&quot;ahbgdc&quot;</code></p>



<p>返回&nbsp;<code>true</code>.</p>



<p><strong>示例&nbsp;2:</strong><br />

<strong>s</strong> = <code>&quot;axc&quot;</code>, <strong>t</strong> = <code>&quot;ahbgdc&quot;</code></p>



<p>返回&nbsp;<code>false</code>.</p>



<p><strong>后续挑战</strong> <strong>:</strong></p>



<p>如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k &gt;= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？</p>



<p><strong>致谢:</strong></p>



<p>特别感谢<strong> </strong><a href="https://leetcode.com/pbrother/">@pbrother&nbsp;</a>添加此问题并且创建所有测试用例。</p>





 **难度**: Easy



 **标签**: 贪心算法、 二分查找、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了39.48% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了88.49% 的用户

解题思路：
    双指针法
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t) :
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False


</code></pre></div>
