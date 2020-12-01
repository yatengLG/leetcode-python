Leetcode 376. 摆动序列
<p>如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为<strong>摆动序列。</strong>第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。</p>


<p>例如，&nbsp;<code>[1,7,4,9,2,5]</code> 是一个摆动序列，因为差值 <code>(6,-3,5,-7,3)</code>&nbsp;是正负交替出现的。相反, <code>[1,4,7,2,5]</code>&nbsp;和&nbsp;<code>[1,7,4,5,5]</code> 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。</p>



<p>给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入: </strong>[1,7,4,9,2,5]

<strong>输出: </strong>6 

<strong>解释: </strong>整个序列均为摆动序列。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入: </strong>[1,17,5,10,13,15,10,5,16,8]

<strong>输出: </strong>7

<strong>解释: </strong>这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。</pre>



<p><strong>示例 3:</strong></p>



<pre><strong>输入: </strong>[1,2,3,4,5,6,7,8,9]

<strong>输出: </strong>2</pre>



<p><strong>进阶:</strong><br>

你能否用&nbsp;O(<em>n</em>) 时间复杂度完成此题?</p>





 **难度**: Medium



 **标签**: 贪心算法、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了90.60% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了68.93% 的用户

解题思路：
    动态规划
    例：  1,17,5,10,13,15,10,5,16,8

            1     17    5    10     13    15    10    5     16    8
        ↗   0   ↗ 1 ↘ → 1   ↗ 3   ↗ 3   ↗ 3 ↘ → 3 ↘ → 3   ↗ 5 ↘ → 5
        ↘   0 ↗ → 0   ↘ 2 ↗ → 2 ↗ → 2 ↗ → 2   ↘ 4   ↘ 4 ↗ → 4   ↘ 6

        n   1     2     3     4     4     4     5     5     6     7

        使用dp[0][i]保存上升的结果，使用dp[1][i]表示下降的结果
        nums[i] > nums[i+1]时，上升
            dp[0][i] = dp[1][i-1] + 1   当前数值在上一个下降时的数值基础上+1
            dp[1][i] = dp[1][i-1]       当前数字下降等于前一个下降时的数值，保持不变
        nums[i] < nums[i+1]时，下降
            dp[0][i] = dp[0][i-1]       当前数值上升等于前一个数上升时的数值，保持不变
            dp[1][i] = dp[0][i-1] + 1   当前数字下降在前一个数上升的数值基础上+1
        nums[i] == nums[i+1]时，等于
            dp[0][i] = dp[0][i - 1]     上升下降均保持不变
            dp[1][i] = dp[1][i - 1]

"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[1][i] = dp[1][i - 1]
                dp[0][i] = dp[1][i - 1] + 1
            elif nums[i] < nums[i-1]:
                dp[1][i] = dp[0][i - 1] + 1
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = dp[1][i - 1]
        return max(dp[0][-1], dp[1][-1])+1</code></pre></div>
