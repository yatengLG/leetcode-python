Leetcode 942. 增减字符串匹配
<p>给定只含&nbsp;<code>&quot;I&quot;</code>（增大）或 <code>&quot;D&quot;</code>（减小）的字符串&nbsp;<code>S</code>&nbsp;，令&nbsp;<code>N = S.length</code>。</p>


<p>返回&nbsp;<code>[0, 1, ..., N]</code>&nbsp;的任意排列&nbsp;<code>A</code>&nbsp;使得对于所有&nbsp;<code>i = 0,&nbsp;..., N-1</code>，都有：</p>



<ul>

	<li>如果&nbsp;<code>S[i] == &quot;I&quot;</code>，那么&nbsp;<code>A[i] &lt; A[i+1]</code></li>

	<li>如果&nbsp;<code>S[i] == &quot;D&quot;</code>，那么&nbsp;<code>A[i] &gt; A[i+1]</code></li>

</ul>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输出：</strong>&quot;IDID&quot;

<strong>输出：</strong>[0,4,1,3,2]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输出：</strong>&quot;III&quot;

<strong>输出：</strong>[0,1,2,3]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输出：</strong>&quot;DDI&quot;

<strong>输出：</strong>[3,2,0,1]</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= S.length &lt;= 10000</code></li>

	<li><code>S</code> 只包含字符&nbsp;<code>&quot;I&quot;</code>&nbsp;或&nbsp;<code>&quot;D&quot;</code>。</li>

</ol>





 **难度**: Easy



 **标签**: 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：4752 ms, 在所有 Python3 提交中击败了5.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了16.67% 的用户

算法思想：
    两个列表，一个保存需要放入的元素， 一个用来存储结果
    如遇到I，则从列表中取出最小值，放入result中
    遇到D，则从列表中取出最大值，放入result中
"""
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        list1 = list(range(len(S) + 1))

        for s in S:
            if s == 'I':
                element = min(list1)
                result.append(element)
                list1.remove(element)
            else:
                element = max(list1)
                result.append(element)
                list1.remove(element)
        result.extend(list1)
        return result


"""
执行用时：76 ms, 在所有 Python3 提交中击败了73.40% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了16.67% 的用户
解题思路：
    由于本题中 需要存入的元素是连续的，所以直接定义俩个变量存储最大值和最小值，省去列表步骤
"""
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        min_, max_ = 0, len(S)
        for s in S:
            if s == 'I':
                result.append(min_)
                min_ += 1
            else:
                result.append(max_)
                max_ -= 1
        result.append(min_)
        return result

</code></pre></div>
