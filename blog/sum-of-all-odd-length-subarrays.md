Leetcode 1588. 所有奇数长度子数组的和
<p>给你一个正整数数组&nbsp;<code>arr</code>&nbsp;，请你计算所有可能的奇数长度子数组的和。</p>


<p><strong>子数组</strong> 定义为原数组中的一个连续子序列。</p>



<p>请你返回 <code>arr</code>&nbsp;中 <strong>所有奇数长度子数组的和</strong> 。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [1,4,2,5,3]

<strong>输出：</strong>58

<strong>解释：</strong>所有奇数长度子数组和它们的和为：

[1] = 1

[4] = 4

[2] = 2

[5] = 5

[3] = 3

[1,4,2] = 7

[4,2,5] = 11

[2,5,3] = 10

[1,4,2,5,3] = 15

我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [1,2]

<strong>输出：</strong>3

<strong>解释：</strong>总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>arr = [10,11,12]

<strong>输出：</strong>66

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= arr.length &lt;= 100</code></li>

	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>

</ul>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：72 ms, 在所有 Python3 提交中击败了56.70% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了25.43% 的用户

解题思路：
    先以奇数长度截取字符串，求和
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = []
        n = len(arr)

        for l in range(1, n+1): # 依次尝试 1~n的长度
            if l%2 == 1:    # 如果当前 长度为奇数
                for j in range(n-l+1):  # 以当前长度截取字符串，求和
                    result.append(sum(arr[j:j+l]))
        return sum(result)

"""
执行用时：72 ms, 在所有 Python3 提交中击败了56.70% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了84.07% 的用户

解题思路：
    先以奇数长度截取字符串，求和
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = []
        n = len(arr)

        for l in range(1, n+1, 2): # 依次尝试 1~n的长度
            for j in range(n-l+1):  # 以当前长度截取字符串，求和
                result.append(sum(arr[j:j+l]))
        return sum(result)

</code></pre></div>
