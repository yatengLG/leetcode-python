Leetcode 215. 数组中的第K个最大元素
<p>在未排序的数组中找到第 <strong>k</strong> 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。</p>


<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong> <code>[3,2,1,5,6,4] 和</code> k = 2

<strong>输出:</strong> 5

</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong> <code>[3,2,3,1,2,4,5,5,6] 和</code> k = 4

<strong>输出:</strong> 4</pre>



<p><strong>说明: </strong></p>



<p>你可以假设 k 总是有效的，且 1 &le; k &le; 数组的长度。</p>





 **难度**: Medium



 **标签**: 堆、 分治算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1732 ms, 在所有 Python3 提交中击败了12.27% 的用户
内存消耗：14 MB, 在所有 Python3 提交中击败了60.77% 的用户

解题思路：
    冒泡排序
    通过判断k与nums的长度，决定排序方向
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return nums[k-1]
        if k > n/2: # 如果 k>nums长度的一半
            for j in range(n-1):
                for i in range(n-1-j):
                    if nums[i] < nums[i + 1]:   # 从大到小拍,每次将最小值放到末尾
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                if j > n-k-1:
                    return nums[k-1]    # 取第k-1个则为第k个最大值
        else:       # 如果大于长度一半
            for j in range(n-1):
                for i in range(n-1-j):
                    if nums[i] > nums[i + 1]:   # 从小到大排,每次将最大值放到末尾
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                if j > k-2:
                    return nums[-k] # 取第-k个即为第k个最大数</code></pre></div>
