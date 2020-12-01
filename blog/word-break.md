Leetcode 139. 单词拆分
<p>给定一个<strong>非空</strong>字符串 <em>s</em> 和一个包含<strong>非空</strong>单词列表的字典 <em>wordDict</em>，判定&nbsp;<em>s</em> 是否可以被空格拆分为一个或多个在字典中出现的单词。</p>


<p><strong>说明：</strong></p>



<ul>

	<li>拆分时可以重复使用字典中的单词。</li>

	<li>你可以假设字典中没有重复的单词。</li>

</ul>



<p><strong>示例 1：</strong></p>



<pre><strong>输入:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;, &quot;code&quot;]

<strong>输出:</strong> true

<strong>解释:</strong> 返回 true 因为 &quot;leetcode&quot; 可以被拆分成 &quot;leet code&quot;。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;, &quot;pen&quot;]

<strong>输出:</strong> true

<strong>解释:</strong> 返回 true 因为 <code>&quot;</code>applepenapple<code>&quot;</code> 可以被拆分成 <code>&quot;</code>apple pen apple<code>&quot;</code>。

&nbsp;    注意你可以重复使用字典中的单词。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]

<strong>输出:</strong> false

</pre>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了45.63% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了86.84% 的用户

解题思路：
    总体的思路是合成，通过两个都匹配的子串，来证明合成的串 可拆分
    依次判断子串是否可以拆分, 双指针依次遍历。若s[:i] and s[i:j] 都可以拆分，则s[0：j]可以拆分

    '' l e e t c o d e
    T  F F F T F F F T
    i
       j
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False for _ in range(n+1)]
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

"""
执行用时：44 ms, 在所有 Python3 提交中击败了90.36% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了65.15% 的用户

解题思路：
    这个是参考leetcode他人提出的思路
    与上例不同在于，上例主要思想是合成，先找到一个匹配的子串，然后向后匹配，再找一个子串，然后合成的子串可拆分 s[:i]+s[i:j] = s[:j]
    遍历一个子串，然后去查看该子串是否可以拆分，若可拆分，则s[:j] + s[j:i] == s[i] 当前子串可拆分
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False for _ in range(n+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]
</code></pre></div>
