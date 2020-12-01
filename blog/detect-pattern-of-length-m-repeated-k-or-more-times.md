Leetcode 1566. 重复至少 K 次且长度为 M 的模式
<p>给你一个正整数数组 <code>arr</code>，请你找出一个长度为 <code>m</code> 且在数组中至少重复 <code>k</code> 次的模式。</p>


<p><strong>模式</strong> 是由一个或多个值组成的子数组（连续的子序列），<strong>连续</strong> 重复多次但 <strong>不重叠</strong> 。 模式由其长度和重复次数定义。</p>



<p>如果数组中存在至少重复 <code>k</code> 次且长度为 <code>m</code> 的模式，则返回 <code>true</code> ，否则返回&nbsp; <code>false</code> 。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [1,2,4,4,4,4], m = 1, k = 3

<strong>输出：</strong>true

<strong>解释：</strong>模式 <strong>(4)</strong> 的长度为 1 ，且连续重复 4 次。注意，模式可以重复 k 次或更多次，但不能少于 k 次。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [1,2,1,2,1,1,1,3], m = 2, k = 2

<strong>输出：</strong>true

<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，且连续重复 2 次。另一个符合题意的模式是 <strong>(2,1) </strong>，同样重复 2 次。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>arr = [1,2,1,2,1,3], m = 2, k = 3

<strong>输出：</strong>false

<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，但是只连续重复 2 次。不存在长度为 2 且至少重复 3 次的模式。

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>arr = [1,2,3,1,2], m = 2, k = 2

<strong>输出：</strong>false

<strong>解释：</strong>模式 <strong>(1,2)</strong> 出现 2 次但并不连续，所以不能算作连续重复 2 次。

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入：</strong>arr = [2,2,2,2], m = 2, k = 3

<strong>输出：</strong>false

<strong>解释：</strong>长度为 2 的模式只有 <strong>(2,2)</strong> ，但是只连续重复 2 次。注意，不能计算重叠的重复次数。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>2 &lt;= arr.length &lt;= 100</code></li>

	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>

	<li><code>1 &lt;= m&nbsp;&lt;= 100</code></li>

	<li><code>2 &lt;= k&nbsp;&lt;= 100</code></li>

</ul>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了90.83% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了91.78% 的用户

解题思路：
    动态规划
    寻找连续重复多次但不重叠的子数组
    例：
        arr = [1,2,1,2,1,1,1,3], m = 2, k = 2

        1   2   1   2   1   1   1   3
        i-m     i       i+m
        0   0   1   1   0   0   0   0

        从m开始遍历
        若arr[i-m:i] == arr[i:i+m]则子数组相同，
            dp[i] = dp[i-m]
    具体实现见代码注释
"""
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)    # 数组长度
        dp = [0 for _ in range(n)]

        for i in range(m, n-m):   # 从m开始遍历,
            if arr[i-m: i] == arr[i:m+i]:   # 若当前其实字符m长度数组与 当前字符前m个字符组成的数组相等
                dp[i] = dp[i-m] + 1

        if max(dp)+1 >= k:
            return True
        else:
            return False

</code></pre></div>
