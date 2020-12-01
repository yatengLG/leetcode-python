Leetcode 303. 区域和检索 - 数组不可变
<p>给定一个整数数组 &nbsp;<em>nums</em>，求出数组从索引&nbsp;<em>i&nbsp;</em>到&nbsp;<em>j&nbsp;&nbsp;</em>(<em>i</em>&nbsp;&le;&nbsp;<em>j</em>) 范围内元素的总和，包含&nbsp;<em>i,&nbsp; j&nbsp;</em>两点。</p>


<p><strong>示例：</strong></p>



<pre>给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()



sumRange(0, 2) -&gt; 1

sumRange(2, 5) -&gt; -1

sumRange(0, 5) -&gt; -3</pre>



<p><strong>说明:</strong></p>



<ol>

	<li>你可以假设数组不可变。</li>

	<li>会多次调用&nbsp;<em>sumRange</em>&nbsp;方法。</li>

</ol>





 **难度**: Easy



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了95.50% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了17.70% 的用户

解题思路：
    动态规划
    ["NumArray","sumRange","sumRange","sumRange"]
    [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

    要求 (i, j)的和，可以看做求(0, j)-(0, i)，前j个的和-前i个的和。
    [-2, 0, 3, -5, 2, -1]
         i

    使用动态规划计算前i个的和
    dp[i] = dp[i-1] + nums[i]

"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n >= 1:
            self.dp = [[] for _ in range(self.n)]
            self.dp[0] = nums[0]
            for i in range(1, self.n):
                self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if self.n < 1:
            return None
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
</code></pre></div>
