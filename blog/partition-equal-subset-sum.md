Leetcode 416. 分割等和子集
<p>给定一个<strong>只包含正整数</strong>的<strong>非空</strong>数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。</p>


<p><strong>注意:</strong></p>



<ol>

	<li>每个数组中的元素不会超过 100</li>

	<li>数组的大小不会超过 200</li>

</ol>



<p><strong>示例 1:</strong></p>



<pre>输入: [1, 5, 11, 5]



输出: true



解释: 数组可以分割成 [1, 5, 5] 和 [11].

</pre>



<p>&nbsp;</p>



<p><strong>示例&nbsp;2:</strong></p>



<pre>输入: [1, 2, 3, 5]



输出: false



解释: 数组不能分割成两个元素和相等的子集.

</pre>



<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1660 ms, 在所有 Python3 提交中击败了44.66% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了55.75% 的用户

解题思路：
    动态规划
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        if sum(nums) % 2 != 0:  # 奇数和 必不能拆分
            return False
        target = int(sum(nums)/2)   # 拆分后的和
        n = len(nums)
        dp = [0] * (target+1)   # 用于记录对应和能否实现
        dp[0] = 1   # 和为0必然可以

        for i in range(n):
            for j in range(target, -1, -1):
                if j+nums[i] <= target:
                    dp[j+nums[i]] = dp[j] or dp[j+nums[i]]  # 原先和+当前数值，即为新的和
            if dp[-1] == 1:
                return True
        return dp[-1] == 1


"""
超时
解题思路：
    回溯1
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()

        def backtrack(begin, current, target, used):
            if target == 0:
                return True
            if target < 0:
                return False

            for i in range(begin, len(nums)):
                if i > 1 and nums[i] == nums[i-1] and i-1 not in used:
                    continue
                if backtrack(i+1, current+[nums[i]], target-nums[i], used+[i]):
                    return True

        target = int(sum(nums) / 2)
        if target * 2 != sum(nums):
            return False

        if target < nums[-1]:
            return False

        if backtrack(0, [], target, []):
            return True
        else:
            return False


"""
超时
解题思路：
    回溯2
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        if max(nums) > target:
            return False

        nums.sort(reverse=True)
        def backtrack(current:int, nums:ist):
            if current == target:
                return True
            if current > target:
                return
            for i in range(len(nums)):
                if backtrack(current+nums[i], nums[i+1:]):
                    return True
            return False
        return backtrack(0, nums)
</code></pre></div>
