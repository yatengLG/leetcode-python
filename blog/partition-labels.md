Leetcode 763. 划分字母区间
<p>字符串 <code>S</code> 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。</p>


<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>S = &quot;ababcbacadefegdehijhklij&quot;

<strong>输出：</strong>[9,7,8]

<strong>解释：</strong>

划分结果为 &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;。

每个字母最多出现在一个片段中。

像 &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; 的划分是错误的，因为划分的片段数较少。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>S</code>的长度在<code>[1, 500]</code>之间。</li>

	<li><code>S</code>只包含小写字母 <code>&#39;a&#39;</code> 到 <code>&#39;z&#39;</code> 。</li>

</ul>





 **难度**: Medium



 **标签**: 贪心算法、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.21% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.01% 的用户

解题思路:
    具体实现见代码注释
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        record = {}
        for i in range(len(S)-1, -1, -1):   # 先遍历字符串，统计各字符出现的最后位置
            if S[i] not in record:
                record[S[i]] = i

        result =[]
        start, end = 0, 0   # 当前划分区间的 起始与结束
        for i, c in enumerate(S):
            end = max(end, record[c])   # 当前区间的结束 以当前区间字符的最后位置为准
            if i == end:    # 如遍历到当前区间内字符的最后位置，则当前区间为一个可划分区间
                result.append(end-start+1)
                start = i+1 # 划分区间后，下次划分的其实start需要移动
        return result
</code></pre></div>
