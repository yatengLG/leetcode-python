Leetcode 1111. 有效括号的嵌套深度
<p><strong>有效括号字符串 </strong>定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「<strong>有效括号字符串</strong>」部分。</p>


<p><strong>嵌套深度</strong> <code>depth</code> 定义：即有效括号字符串嵌套的层数，<code>depth(A)</code> 表示有效括号字符串 <code>A</code> 的嵌套深度。详情参见题末「<strong>嵌套深度</strong>」部分。</p>



<p>有效括号字符串类型与对应的嵌套深度计算方法如下图所示：</p>



<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/01/1111.png" style="height: 152px; width: 600px;"></p>



<p>&nbsp;</p>



<p>给你一个「有效括号字符串」 <code>seq</code>，请你将其分成两个不相交的有效括号字符串，<code>A</code> 和&nbsp;<code>B</code>，并使这两个字符串的深度最小。</p>



<ul>

	<li>不相交：每个 <code>seq[i]</code> 只能分给 <code>A</code> 和 <code>B</code> 二者中的一个，不能既属于 <code>A</code> 也属于 <code>B</code> 。</li>

	<li><code>A</code> 或 <code>B</code> 中的元素在原字符串中可以不连续。</li>

	<li><code>A.length + B.length = seq.length</code></li>

	<li>深度最小：<code>max(depth(A), depth(B))</code>&nbsp;的可能取值最小。&nbsp;</li>

</ul>



<p>划分方案用一个长度为 <code>seq.length</code> 的答案数组 <code>answer</code> 表示，编码规则如下：</p>



<ul>

	<li><code>answer[i] = 0</code>，<code>seq[i]</code> 分给 <code>A</code> 。</li>

	<li><code>answer[i] = 1</code>，<code>seq[i]</code> 分给 <code>B</code> 。</li>

</ul>



<p>如果存在多个满足要求的答案，只需返回其中任意 <strong>一个 </strong>即可。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>seq = &quot;(()())&quot;

<strong>输出：</strong>[0,1,1,1,1,0]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>seq = &quot;()(())()&quot;

<strong>输出：</strong>[0,0,0,1,1,0,1,1]

<strong>解释：</strong>本示例答案不唯一。

按此输出 A = &quot;()()&quot;, B = &quot;()()&quot;, max(depth(A), depth(B)) = 1，它们的深度最小。

像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = &quot;()()()&quot;, B = &quot;()&quot;, max(depth(A), depth(B)) = 1 。 

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;&nbsp;seq.size &lt;= 10000</code></li>

</ul>



<p>&nbsp;</p>



<p><strong>有效括号字符串：</strong></p>



<pre>仅由&nbsp;<code>&quot;(&quot;</code> 和&nbsp;<code>&quot;)&quot;</code>&nbsp;构成的字符串，对于每个左括号，都能找到与之对应的右括号，反之亦然。

下述几种情况同样属于有效括号字符串：



  1. 空字符串

  2. 连接，可以记作&nbsp;<code>AB</code>（<code>A</code> 与 <code>B</code> 连接），其中&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都是有效括号字符串

  3. 嵌套，可以记作&nbsp;<code>(A)</code>，其中&nbsp;<code>A</code>&nbsp;是有效括号字符串

</pre>



<p><strong>嵌套深度：</strong></p>



<pre>类似地，我们可以定义任意有效括号字符串 <code>s</code> 的 <strong>嵌套深度</strong>&nbsp;<code>depth(S)</code>：



  1.<code> s</code> 为空时，<code>depth(&quot;&quot;) = 0</code>

<code>  2. s</code> 为 <code>A</code> 与 <code>B</code> 连接时，<code>depth(A + B) = max(depth(A), depth(B))</code>，其中&nbsp;<code>A</code> 和&nbsp;<code>B</code>&nbsp;都是有效括号字符串

<code>  3. s</code> 为嵌套情况，<code>depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A)</code>，其中 <code>A</code> 是有效括号字符串



例如：<code>&quot;&quot;</code>，<code>&quot;()()&quot;</code>，和&nbsp;<code>&quot;()(()())&quot;</code>&nbsp;都是有效括号字符串，嵌套深度分别为 0，1，2，而&nbsp;<code>&quot;)(&quot;</code> 和&nbsp;<code>&quot;(()&quot;</code>&nbsp;都不是有效括号字符串。

</pre>





 **难度**: Medium



 **标签**: 贪心算法、 二分查找、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了98.57% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了10.68% 的用户

解题思路：
    先统计括号嵌套深度，然后进行分配
"""
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        d, max_d = 0, 0 # 当前深度，最大深度
        result = []
        for s in seq:
            max_d = max(d, max_d)
            if s == "(":    # 左括号
                d += 1      # 先深度+1
                result.append(d)    # 然后将当前括号深度添加到结果中
            if s == ")":    # 右括号
                result.append(d)    # 先将当前括号深度添加到结果中
                d -= 1              # 然后深度-1
        max_ = max_d//2 # 以深度，分为两部分
        result = [1 if r > max_ else 0 for r in result ] # 重新整理结果
        return result
</code></pre></div>
