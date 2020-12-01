Leetcode 5. 最长回文子串
<p>给定一个字符串 <code>s</code>，找到 <code>s</code> 中最长的回文子串。你可以假设&nbsp;<code>s</code> 的最大长度为 1000。</p>


<p><strong>示例 1：</strong></p>



<pre><strong>输入:</strong> &quot;babad&quot;

<strong>输出:</strong> &quot;bab&quot;

<strong>注意:</strong> &quot;aba&quot; 也是一个有效答案。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入:</strong> &quot;cbbd&quot;

<strong>输出:</strong> &quot;bb&quot;

</pre>





 **难度**: Medium



 **标签**: 字符串、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG
"""
执行用时：804 ms, 在所有 Python3 提交中击败了87.08% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了9.26% 的用户

算法思想：
    使用了中心扩散的思想：
    具体实现见代码注释

注： Manacher 算法 速度更快，但更为复杂，有兴趣可以了解一下
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        string = ""

        for m in range(n):  # 从字符串起始开始进行遍历，m为当前字符串中心， 但字符必定回文
            p, q = m, m     # 初始俩个指针，指向该回文字符，两指针会一个左移、一个右移，用于判断扩散后的字符串是否回文
            while s[q] == s[m]: # 判断该字符相邻字符是否相等，若相等，则将右指针右移。这是为了处理abba形式，以bb为中心的偶数回文
                q += 1
                if q > n-1:
                    break
            q -= 1

            while s[p] == s[q]: # 判断两指针所指字符是否相等，若相等，则指针内部字符串回文，指针扩散
                p -= 1
                q += 1
                if (p < 0) or (q > n-1):    # 指针超出字符串索引，跳出循环
                    break
            if len(string) < q-p-1: # 对比当前指针内部字符串与记录的回文字符串
                string = s[p+1:q]
        return string


"""
执行用时：4852 ms, 在所有 Python3 提交中击败了32.82% 的用户
内存消耗：21.4 MB, 在所有 Python3 提交中击败了5.55% 的用户

解题思路：
    使用了动态规划的思想。
    具体看代码注释
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        string = ""
        dp = [[False] * n for _ in range(n)]    # 一个矩阵，用于存储对于 起始下标i到结尾下标j对应字符串 是否回文

        for j in range(n):  # 从开始一次遍历 0, 1, 2, ... ,n
            for i in range(j+1):    # 只需遍历一半，下标(i, j)：(0, 0), (0, 1), (1, 1), (0, 2), (1, 2), ...
                if i == j:          # 对角线为单字符，必定回文
                    dp[i][j] = True
                if j-i > 2:         # 若下标间距大于2， 即abaa， 下标中间不止一个字符，则判断俩字符是否相等，且中间部分是否回文
                    dp[i][j] = (((s[i] == s[j]) and dp[i+1][j-1]))
                else:               # 若下标间距不大于2，即aba， 则只需判断下标对应字符是否相等即可判断是否回文
                    dp[i][j] = (s[i] == s[j])
                if dp[i][j] and j+1-i > len(string):    # 若当前下标间的字符串回文，则对比记录的字符串，且比较长度
                    string = s[i: j+1]
        return string</code></pre></div>
