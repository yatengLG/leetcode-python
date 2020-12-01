Leetcode 1441. 用栈操作构建数组
<p>给你一个目标数组 <code>target</code> 和一个整数 <code>n</code>。每次迭代，需要从&nbsp; <code>list = {1,2,3..., n}</code> 中依序读取一个数字。</p>


<p>请使用下述操作来构建目标数组 <code>target</code> ：</p>



<ul>

	<li><strong>Push</strong>：从 <code>list</code> 中读取一个新元素， 并将其推入数组中。</li>

	<li><strong>Pop</strong>：删除数组中的最后一个元素。</li>

	<li>如果目标数组构建完成，就停止读取更多元素。</li>

</ul>



<p>题目数据保证目标数组严格递增，并且只包含 <code>1</code> 到 <code>n</code> 之间的数字。</p>



<p>请返回构建目标数组所用的操作序列。</p>



<p>题目数据保证答案是唯一的。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>target = [1,3], n = 3

<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;]

<strong>解释： 

</strong>读取 1 并自动推入数组 -&gt; [1]

读取 2 并自动推入数组，然后删除它 -&gt; [1]

读取 3 并自动推入数组 -&gt; [1,3]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>target = [1,2,3], n = 3

<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>target = [1,2], n = 4

<strong>输出：</strong>[&quot;Push&quot;,&quot;Push&quot;]

<strong>解释：</strong>只需要读取前 2 个数字就可以停止。

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>target = [2,3,4], n = 4

<strong>输出：</strong>[&quot;Push&quot;,&quot;Pop&quot;,&quot;Push&quot;,&quot;Push&quot;,&quot;Push&quot;]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= target.length &lt;= 100</code></li>

	<li><code>1 &lt;= target[i]&nbsp;&lt;= 100</code></li>

	<li><code>1 &lt;= n &lt;= 100</code></li>

	<li><code>target</code> 是严格递增的</li>

</ul>





 **难度**: Easy



 **标签**: 栈、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.57% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了38.43% 的用户

解题思路：
    用下标去查看target元素
    见代码注释
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        N = len(target)
        result = []
        for num in range(1, n+1):
            if num == target[i]:
                i += 1
                result.append('Push')   # 如果数组与元素符合，则push,且对比下一个元素
            else:
                result.append('Push')
                result.append('Pop')
                # result.extend(['Push', 'Pop'])  # 不符合，则push后pop, 用下一个数字对比
            if i > N-1:
                break
        return result

</code></pre></div>
