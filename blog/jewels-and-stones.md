Leetcode 771. 宝石与石头
<p>&nbsp;给定字符串<code>J</code>&nbsp;代表石头中宝石的类型，和字符串&nbsp;<code>S</code>代表你拥有的石头。&nbsp;<code>S</code>&nbsp;中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。</p>


<p><code>J</code>&nbsp;中的字母不重复，<code>J</code>&nbsp;和&nbsp;<code>S</code>中的所有字符都是字母。字母区分大小写，因此<code>&quot;a&quot;</code>和<code>&quot;A&quot;</code>是不同类型的石头。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> J = &quot;aA&quot;, S = &quot;aAAbbbb&quot;

<strong>输出:</strong> 3

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong> J = &quot;z&quot;, S = &quot;ZZ&quot;

<strong>输出:</strong> 0

</pre>



<p><strong>注意:</strong></p>



<ul>

	<li><code>S</code>&nbsp;和&nbsp;<code>J</code>&nbsp;最多含有50个字母。</li>

	<li>&nbsp;<code>J</code>&nbsp;中的字符不重复。</li>

</ul>





 **难度**: Easy



 **标签**: 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了89.80% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了72.55%

解题思路：
    先遍历宝石类别，
    然后遍历石头，统计各宝石数量
"""
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_dic = {}  # 各宝石数量
        for j in J:
            jewel_dic[j] = 0    # 遍历宝石类别，各宝石数量起始为0

        for s in S: # 遍历石头
            if s in jewel_dic:  # 对应宝石数量+1
                jewel_dic[s] += 1
        return sum(jewel_dic.values())</code></pre></div>
