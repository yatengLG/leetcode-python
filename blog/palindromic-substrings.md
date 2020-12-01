Leetcode 647. 回文子串
<p>给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。</p>


<p>具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>&quot;abc&quot;

<strong>输出：</strong>3

<strong>解释：</strong>三个回文子串: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>&quot;aaa&quot;

<strong>输出：</strong>6

<strong>解释：</strong>6个回文子串: &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;aa&quot;, &quot;aa&quot;, &quot;aaa&quot;</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>输入的字符串长度不会超过 1000 。</li>

</ul>





 **难度**: Medium



 **标签**: 字符串、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：648 ms, 在所有 Python3 提交中击败了9.86% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了79.30% 的用户

解题思路：
    暴力法, 双指针暴力拆解
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num = 0
        for i in range(n):
            for j in range(i, n):
                string = s[i:j+1]
                if string == string[::-1]:
                    num += 1
        return num

"""
执行用时：164 ms, 在所有 Python3 提交中击败了65.42% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了62.96% 的用户

解题思路：
    中心扩展, 需分析两种情况    xax, xaax 以单个字符为中心，以两个字符为中心
    详见代码注释
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        num = 0
        i = 0
        while i < n:        # i指针，依次遍历字符串
            num += 1        # 每个单独的字符都回文
            l, r = i, i     # 以当前字符为中心，向两侧扩展
            while l-1 >= 0 and r+1 < n:
                if s[l-1] == s[r+1]:    # 判断字符两侧是否相同，若相同，则该字符串回文
                    num += 1
                    l = l-1             # 相同继续扩展
                    r = r+1
                else:
                    break               # 不相同，则跳出循环，遍历下一个字符

            if i+1<n and s[i+1] == s[i]:    # 判断当前点与下一个点是否相同，若相同，则相邻两字符回文
                num += 1                    # 若相同，则相邻两字符回文
                l, r = i, i+1               # 以两字符开始向外扩展

                while l - 1 >= 0 and r + 1 < n:
                    if s[l - 1] == s[r + 1]:    # 两侧字符相同，则组成的字符串回文
                        num += 1
                        l = l - 1               # 继续扩展
                        r = r + 1
                    else:
                        break
            i += 1
        return num

</code></pre></div>
