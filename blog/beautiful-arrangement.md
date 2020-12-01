Leetcode 526. 优美的排列
<p>假设有从 1 到 N 的&nbsp;<strong>N&nbsp;</strong>个整数，如果从这&nbsp;<strong>N&nbsp;</strong>个数字中成功构造出一个数组，使得数组的第 <strong>i</strong>&nbsp;位 (1 &lt;= i &lt;= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：</p>


<ol>

	<li>第&nbsp;<strong>i&nbsp;</strong>位的数字能被&nbsp;<strong>i&nbsp;</strong>整除</li>

	<li><strong>i</strong> 能被第 <strong>i</strong> 位上的数字整除</li>

</ol>



<p>现在给定一个整数 N，请问可以构造多少个优美的排列？</p>



<p><strong>示例1:</strong></p>



<pre>

<strong>输入:</strong> 2

<strong>输出:</strong> 2

<strong>解释:</strong> 



第 1 个优美的排列是 [1, 2]:

  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除

  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除



第 2 个优美的排列是 [2, 1]:

  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除

  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除

</pre>



<p><strong>说明:</strong></p>



<ol>

	<li><strong>N</strong> 是一个正整数，并且不会超过15。</li>

</ol>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：3088 ms, 在所有 Python3 提交中击败了5.31% 的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了5.19% 的用户

解题思路：
    回溯
    出版，使用current存放当前列表，通过len(current)获取即将插入的下标
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current):
            # print(current)
            if len(current) == N:
                result.append(current[:])
                return

            for i in range(N):
                if nums[i] not in current and (nums[i] % (len(current)+1) == 0  or (len(current)+1) % nums[i] == 0):
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()

        backtrack([])
        return len(result)

"""
执行用时：2536 ms, 在所有 Python3 提交中击败了9.78% 的用户
内存消耗：21.8 MB, 在所有 Python3 提交中击败了5.19% 的用户

优化思路：
    直接从nums中取数字，可以提升一部分
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current):
            if len(current) == N:
                result.append(current[:])
                return

            for num in nums:
                if num not in current and (num % (len(current)+1) == 0  or (len(current)+1) % num == 0):
                    current.append(num)
                    backtrack(current)
                    current.pop()

        backtrack([])
        return len(result)

"""
执行用时：2240 ms, 在所有 Python3 提交中击败了15.64% 的用户
内存消耗：21.6 MB, 在所有 Python3 提交中击败了5.19% 的用户

优化思路：
    使用一个单独的index变量，记录存储在列表中的位置。
"""
class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result = []

        def backtrack(current, index):
            if len(current) == N:
                result.append(current[:])
                return

            for num in nums:
                if num not in current and (num % index == 0  or index % num == 0):
                    current.append(num)
                    backtrack(current, index+1)
                    current.pop()

        backtrack([], 1)
        return len(result)
</code></pre></div>
