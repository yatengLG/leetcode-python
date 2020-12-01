Leetcode 91. 解码方法
<p>一条包含字母&nbsp;<code>A-Z</code> 的消息通过以下方式进行了编码：</p>


<pre>&#39;A&#39; -&gt; 1

&#39;B&#39; -&gt; 2

...

&#39;Z&#39; -&gt; 26

</pre>



<p>给定一个只包含数字的<strong>非空</strong>字符串，请计算解码方法的总数。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> &quot;12&quot;

<strong>输出:</strong> 2

<strong>解释:</strong>&nbsp;它可以解码为 &quot;AB&quot;（1 2）或者 &quot;L&quot;（12）。

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> &quot;226&quot;

<strong>输出:</strong> 3

<strong>解释:</strong>&nbsp;它可以解码为 &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), 或者 &quot;BBF&quot; (2 2 6) 。

</pre>





 **难度**: Medium



 **标签**: 字符串、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了94.07% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了85.98% 的用户

解题思路：
    本题分以下几种情况：
        1. ""                       # 0
        2. "_" 1 ~ 9                # 1
        3. 'x10'                    # dp[i-2]
        4. 'x1_' x11 ~ x19          # dp[i-1] + dp[i-2]
        5. 'x20'                    # dp[i-2]
        6. 'x2_' x21 ~ x26          # dp[i-1] + dp[i-2]
        7. 'x2_' x27 ~ x29          # dp[i-1]
        8. 'x3_' x31 ~ x39          # dp[i-1]
        9. 'x30'                    # 0
       11. 'x00'                    # 0
       10. 'x0_' x01 ~ x09          # dp[i-1]
    分别处理即可
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0 or s[0] == '0':
            return 0

        dp = [[] for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        if n == 1:
            return dp[1]

        for i in range(1, n):
            if s[i-1] == '0':   # 0_
                if s[i] == '0':     # x00
                    return 0
                else:               # x01 x02 x03 ~ x09
                    dp[i+1] = dp[i+1-1]
            elif s[i-1] == '1':     # x1_
                if s[i] == '0':     # x10
                    dp[i+1] = dp[i+1-2]
                else:               # x11 ~ x19
                    dp[i+1] = dp[i+1-1] + dp[i+1-2]
            elif s[i-1] == '2':     # x2_
                if s[i] == '0':  # x20
                    dp[i+1] = dp[i+1-2]
                elif s[i] in '789': # x27 ~ x29
                    dp[i+1] = dp[i+1-1]
                else:               # x21 ~ x26
                    dp[i+1] = dp[i+1-1] + dp[i+1-2]
            else:                   # x3_ ~ x9~
                if s[i] == '0':
                    return 0
                else:
                    dp[i+1] = dp[i+1-1]
        return dp[-1]</code></pre></div>
