Leetcode 1415. 长度为 n 的开心字符串中字典序第 k 小的字符串
<p>一个 「开心字符串」定义为：</p>


<ul>

	<li>仅包含小写字母&nbsp;<code>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code>.</li>

	<li>对所有在&nbsp;<code>1</code>&nbsp;到&nbsp;<code>s.length - 1</code>&nbsp;之间的&nbsp;<code>i</code>&nbsp;，满足&nbsp;<code>s[i] != s[i + 1]</code>&nbsp;（字符串的下标从 1 开始）。</li>

</ul>



<p>比方说，字符串&nbsp;<strong>&quot;abc&quot;</strong>，<strong>&quot;ac&quot;，&quot;b&quot;</strong> 和&nbsp;<strong>&quot;abcbabcbcb&quot;</strong>&nbsp;都是开心字符串，但是&nbsp;<strong>&quot;aa&quot;</strong>，<strong>&quot;baa&quot;</strong>&nbsp;和&nbsp;<strong>&quot;ababbc&quot;</strong>&nbsp;都不是开心字符串。</p>



<p>给你两个整数 <code>n</code>&nbsp;和 <code>k</code>&nbsp;，你需要将长度为 <code>n</code>&nbsp;的所有开心字符串按字典序排序。</p>



<p>请你返回排序后的第 k 个开心字符串，如果长度为 <code>n</code>&nbsp;的开心字符串少于 <code>k</code>&nbsp;个，那么请你返回 <strong>空字符串</strong>&nbsp;。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>n = 1, k = 3

<strong>输出：</strong>&quot;c&quot;

<strong>解释：</strong>列表 [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 &quot;c&quot; 。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>n = 1, k = 4

<strong>输出：</strong>&quot;&quot;

<strong>解释：</strong>长度为 1 的开心字符串只有 3 个。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>n = 3, k = 9

<strong>输出：</strong>&quot;cab&quot;

<strong>解释：</strong>长度为 3 的开心字符串总共有 12 个 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;] 。第 9 个字符串为 &quot;cab&quot;

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>n = 2, k = 7

<strong>输出：</strong>&quot;&quot;

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入：</strong>n = 10, k = 100

<strong>输出：</strong>&quot;abacbabacb&quot;

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= n &lt;= 10</code></li>

	<li><code>1 &lt;= k &lt;= 100</code></li>

</ul>



<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：224 ms, 在所有 Python3 提交中击败了19.92% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了27.04% 的用户

解题思路：
    回溯
    找出所有的结果
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letter = ['a', 'b', 'c']
        result = []

        def backtrack(current):
            if len(current) >= n:   # 长度限定，如果长度达到n,则添加到最终结果，并终止
                result.append(''.join(current))
                return

            for i in range(3):
                if current == [] or (letter[i] != current[-1]): # 当前列表为[] 或 当前字母与当前列表最后一个不同时， 添加到当前列表
                    current.append(letter[i])
                    backtrack(current)
                    current.pop()   # 回溯

        backtrack([])
        if k > len(result):
            return ''
        else:
            return result[k-1]

"""
执行用时：40 ms, 在所有 Python3 提交中击败了94.74% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了93.71% 的用户

解题思路：
    分析状态，找规律
    
    1   a       b       c
    2   ab      ac      ba      bc      ca      cb
    3   aba     abc     aca     acb     bab     bac     bca     bcb     cab     cac     cba     cbc
    4   abab    abac    abca    abcb    acab    acac    acba    acbc    baba    babc    baca    bacb    ...

                  all               a开头     b开头     c开头
    1       3*2**(1-1) = 3*1        1           1       1    
    2       3*2**(2-1) = 3*2        2           2       2
    3       3*2**(3-1) = 3*4        4           4       4
    4       3*2**(4-1) = 3*8        8           8       8
    10      3*2**(10-1)= 3*512      512         512     512    
    需注意的是，当以b开头时，第一个字符是a，第二个是c,需将上一位存在的元素剔除
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        all_num = 3 * 2 ** (n - 1)
        if k > all_num:
            return ''
        result = []

        def find(i, k, pre):    # 当前为位数，当前找第几个数，前一个字符
            letters = ['a', 'b', 'c']
            if pre in letters:
                letters.remove(pre) # 从a,b,c 中移除，上一个字符。确保相邻元素不同
            index = k // 2 ** (n - 1 - i)   # 整除获得下标，依据下标取当前位的字符
            k = k % 2 ** (n - 1 - i)        # 余数，作为新的k
            result.append(letters[index])
            return k, letters[index]

        pre = ''
        k = k - 1
        for i in range(n):
            k, pre = find(i, k, pre)
        return ''.join(result)
</code></pre></div>
