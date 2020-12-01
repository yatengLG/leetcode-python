Leetcode 300. 最长上升子序列
<p>给定一个无序的整数数组，找到其中最长上升子序列的长度。</p>


<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> <code>[10,9,2,5,3,7,101,18]

</code><strong>输出: </strong>4 

<strong>解释: </strong>最长的上升子序列是&nbsp;<code>[2,3,7,101]，</code>它的长度是 <code>4</code>。</pre>



<p><strong>说明:</strong></p>



<ul>

	<li>可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。</li>

	<li>你算法的时间复杂度应该为&nbsp;O(<em>n<sup>2</sup></em>) 。</li>

</ul>



<p><strong>进阶:</strong> 你能将算法的时间复杂度降低到&nbsp;O(<em>n</em> log <em>n</em>) 吗?</p>





 **难度**: Medium



 **标签**: 二分查找、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1052 ms, 在所有 Python3 提交中击败了63.37% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了15.97% 的用户

解题思路：
    i'm stupid!
    参照的官网给的思路写的
    当遍历到一个字符时，必须挨着去与前面的进行比较，然后得出该字符之前的子序列最大长度

    还有其他更快的解法，但由于当前主要在练习动态规划
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [[] for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            max_ = -1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_ = max(max_, dp[j])
            if max_ == -1:
                dp[i] = 1
            else:
                dp[i] = max_ + 1
        return max(dp)


"""
执行用时：40 ms, 在所有 Python3 提交中击败了99.67% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了70.80% 的用户
解题思路：
    贪心算法
    具体实现见代码注释
    为了使上升子序列尽可能的长， 
    等同于使 上升子序列上升速度尽可能慢,
    等同于，每次添加进子序列的值，要尽可能小
    
    例：  [4,10,4,3,8,9]
        num     records
        4       4
        10      4,10
        4       4,10
        3       3,10
        8       3,8
        9       3,8,9
                size = 3
    
    例：  [10,9,2,5,3,7,101,18]
    
        num     records
        10      10
        9       9
        2       2
        5       2,5
        3       2,3
        7       2,3,7
        101     2,3,7,101
        8       2,3,7,18
                size = 4
    
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:       # 如果 长度为0 或为1， 直接返回 0 or 1
            return n
        size = 1            # 初始长度为1
        records = [nums[0]] # 记录列表的第一个元素
        for num in nums[1:]:    # 从第二个元素开始比较
            if num > records[-1]:   # 如果，当前数字，比记录的最大值大，则进列表， 长度+1
                records.append(num)
                size += 1
            else:
                for i, record in enumerate(records):    # 否则，比较记录的元素，使用数字替换大于该数字的第一个记录
                    if num <= record:
                        records[i] = num
                        break
        return size</code></pre></div>
