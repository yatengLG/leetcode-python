Leetcode 面试题 17.10. 主要元素
<p>数组中占比超过一半的元素称之为主要元素。给定一个<strong>整数</strong>数组，找到它的主要元素。若没有，返回-1。</p>


<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[1,2,5,9,5,9,5,5,5]

<strong>输出：</strong>5</pre>



<p>&nbsp;</p>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[3,2]

<strong>输出：</strong>-1</pre>



<p>&nbsp;</p>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>[2,2,1,1,1,2,2]

<strong>输出：</strong>2</pre>



<p>&nbsp;</p>



<p><strong>说明：</strong><br>

你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？</p>





 **难度**: Easy



 **标签**: 位运算、 数组、 分治算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了83.86% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了62.52%

解题思路：
    对拼消耗，摩尔投票
    时间复杂度为 O(N)，空间复杂度为 O(1)
    不同数字一一对拼消耗，如果有剩余，则存在主要元素(人数最多，且，人数在一半以上)
    具体实现见代码注释
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = nums[0] # 记录当前元素
        count = 0   # 当前元素的出现次数统计
        for i in range(n):
            if nums[i] == major:    # 如果与当前元素相同，则次数+1
                count += 1
            else:   # 不同，则对拼消耗，次数减一
                count -= 1
            if count == 0 and i < n-1:  # 如果当前元素被消耗殆尽，当前元素指向下一个元素
                major = nums[i+1]

        if count > 0:   # 如果当前元素的统计次数大于0，则存在主要元素
            return major
        else:       # 否则，不存在
            return -1
</code></pre></div>
