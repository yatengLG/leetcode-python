Leetcode 1207. 独一无二的出现次数
<p>给你一个整数数组&nbsp;<code>arr</code>，请你帮忙统计数组中每个数的出现次数。</p>


<p>如果每个数的出现次数都是独一无二的，就返回&nbsp;<code>true</code>；否则返回 <code>false</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [1,2,2,1,1,3]

<strong>输出：</strong>true

<strong>解释：</strong>在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [1,2]

<strong>输出：</strong>false

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>arr = [-3,0,1,-3,1,1,1,-3,10,0]

<strong>输出：</strong>true

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= arr.length&nbsp;&lt;= 1000</code></li>

	<li><code>-1000 &lt;= arr[i] &lt;= 1000</code></li>

</ul>





 **难度**: Easy



 **标签**: 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了95.14% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了5.42% 的用户

解题思路：
    先统计每个数出现的次数
    然后查看次数是否存在重复
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        record = {}
        for a in arr:
            if a in record:
                record[a] += 1
            else:
                record[a] = 1
        return len(record.values()) == len(set(record.values()))</code></pre></div>
