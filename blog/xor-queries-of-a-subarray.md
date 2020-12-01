Leetcode 1310. 子数组异或查询
<p>有一个正整数数组&nbsp;<code>arr</code>，现给你一个对应的查询数组&nbsp;<code>queries</code>，其中&nbsp;<code>queries[i] = [L<sub>i,&nbsp;</sub>R<sub>i</sub>]</code>。</p>


<p>对于每个查询&nbsp;<code>i</code>，请你计算从&nbsp;<code>L<sub>i</sub></code>&nbsp;到&nbsp;<code>R<sub>i</sub></code>&nbsp;的&nbsp;<strong>XOR</strong>&nbsp;值（即&nbsp;<code>arr[L<sub>i</sub>] <strong>xor</strong> arr[L<sub>i+1</sub>] <strong>xor</strong> ... <strong>xor</strong> arr[R<sub>i</sub>]</code>）作为本次查询的结果。</p>



<p>并返回一个包含给定查询&nbsp;<code>queries</code>&nbsp;所有结果的数组。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]

<strong>输出：</strong>[2,7,14,8] 

<strong>解释：</strong>

数组中元素的二进制表示形式是：

1 = 0001 

3 = 0011 

4 = 0100 

8 = 1000 

查询的 XOR 值为：

[0,1] = 1 xor 3 = 2 

[1,2] = 3 xor 4 = 7 

[0,3] = 1 xor 3 xor 4 xor 8 = 14 

[3,3] = 8

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]

<strong>输出：</strong>[8,0,4,4]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= arr.length &lt;= 3 *&nbsp;10^4</code></li>

	<li><code>1 &lt;= arr[i] &lt;= 10^9</code></li>

	<li><code>1 &lt;= queries.length &lt;= 3 * 10^4</code></li>

	<li><code>queries[i].length == 2</code></li>

	<li><code>0 &lt;= queries[i][0] &lt;= queries[i][1] &lt; arr.length</code></li>

</ul>





 **难度**: Medium



 **标签**: 位运算、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：468 ms, 在所有 Python3 提交中击败了85.90% 的用户
内存消耗：28 MB, 在所有 Python3 提交中击败了5.88% 的用户

解题思路：
    a^b = c
    c^a = b
    c^b = a
    先记录0~n的异或值
    然后，[q,p] 的异或值 = record[p] ^ record[q-1]
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        record = {-1:0}
        for i, a in enumerate(arr):
            record[i] = record[i-1] ^ arr[i]    # 记录每一位之前的异或值
        for q in queries:
            result.append(record[q[1]]^record[q[0]-1])  # 直接计算异或值   # a^b=c c^a=b c^b=a
        return result
</code></pre></div>
