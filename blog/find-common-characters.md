Leetcode 1002. 查找常用字符
<p>给定仅有小写字母组成的字符串数组 <code>A</code>，返回列表中的每个字符串中都显示的全部字符（<strong>包括重复字符</strong>）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。</p>


<p>你可以按任意顺序返回答案。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[&quot;bella&quot;,&quot;label&quot;,&quot;roller&quot;]

<strong>输出：</strong>[&quot;e&quot;,&quot;l&quot;,&quot;l&quot;]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[&quot;cool&quot;,&quot;lock&quot;,&quot;cook&quot;]

<strong>输出：</strong>[&quot;c&quot;,&quot;o&quot;]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= A.length &lt;= 100</code></li>

	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>

	<li><code>A[i][j]</code> 是小写字母</li>

</ol>





 **难度**: Easy



 **标签**: 数组、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了76.09% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.57% 的用户

解题思路：
    使用字典，记录每次
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        record = {i: float('inf') for i in 'abcdefghijklmnopqrstuvwxyz'}    # 用于记录各字符出现次数
        for a in A:
            record_now = {} # 当前单词各字符出现次数
            for i in a:
                if i in record_now:
                    record_now[i] += 1
                else:
                    record_now[i] = 1
            record = {i:min(n, record_now[i]) for i,n in record.items() if i in record_now} # 比较当前单词字符出现次数，更新record

        return [i for i,n in record.items() for _ in range(n)]
</code></pre></div>
