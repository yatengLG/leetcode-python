Leetcode 55. 跳跃游戏
<p>给定一个非负整数数组，你最初位于数组的第一个位置。</p>


<p>数组中的每个元素代表你在该位置可以跳跃的最大长度。</p>



<p>判断你是否能够到达最后一个位置。</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong> [2,3,1,1,4]

<strong>输出:</strong> true

<strong>解释:</strong> 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> [3,2,1,0,4]

<strong>输出:</strong> false

<strong>解释:</strong> 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

</pre>





 **难度**: Medium



 **标签**: 贪心算法、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了83.73% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了9.98% 的用户

解题思路：
    当前点能到达的最远点决定了当前点能到达的范围
    只有能到达的最远点比结尾远，就一定能到达
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0 # 能到达的最远点
        for i, num in enumerate(nums):
            if i <= far:    # 如果当前点，现在能到达
                far = max(far, i+num)   # 更新能到达的最远点
        return far >= i # 比较能到达的最远点与列表长度</code></pre></div>
