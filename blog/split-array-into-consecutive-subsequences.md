Leetcode 659. 分割数组为连续子序列
<p>给你一个按升序排序的整数数组 <code>num</code>（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。</p>


<p>如果可以完成上述分割，则返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入:</strong> [1,2,3,3,4,5]

<strong>输出:</strong> True

<strong>解释:</strong>

你可以分割出这样两个连续子序列 : 

1, 2, 3

3, 4, 5

</pre>



<p>&nbsp;</p>



<p><strong>示例 2：</strong></p>



<pre><strong>输入:</strong> [1,2,3,3,4,4,5,5]

<strong>输出:</strong> True

<strong>解释:</strong>

你可以分割出这样两个连续子序列 : 

1, 2, 3, 4, 5

3, 4, 5

</pre>



<p>&nbsp;</p>



<p><strong>示例 3：</strong></p>



<pre><strong>输入:</strong> [1,2,3,4,4,5]

<strong>输出:</strong> False

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li>输入的数组长度范围为 [1, 10000]</li>

</ol>



<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 堆、 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了90.08% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了43.72% 的用户

"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)    # 统计nums中每个数的出现次数
        endMap = collections.Counter()  # 统计以num结尾的子序列的个数

        for num in nums:
            if countMap[num]:
                if endMap.get(num-1):   # 如果存在子序列以 num-1 结尾，则，把当前数 添加到该序列后
                    countMap[num] -= 1  # 当前数统计次数-1
                    endMap[num-1] -= 1  # 以num-1为结尾的子序列-1
                    endMap[num] += 1    # 以num为结尾的子序列+1
                else:
                    if countMap.get(num+1) and countMap.get(num+2): # 如果num, num+1, num+2 均存在，则此三个数构成一个新的子序列
                        endMap[num+2] += 1      # 以num+2为结尾的子序列+1
                        countMap[num] -= 1      # num统计次数-1
                        countMap[num+1] -= 1    # num+1统计次数-1
                        countMap[num+2] -= 1    # num+2统计次数-1
                    else:
                        return False
        return True

</code></pre></div>
