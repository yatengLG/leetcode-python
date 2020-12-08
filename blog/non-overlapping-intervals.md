Leetcode 435. 无重叠区间
<p>给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。</p>


<p><strong>注意:</strong></p>



<ol>

	<li>可以认为区间的终点总是大于它的起点。</li>

	<li>区间 [1,2] 和 [2,3] 的边界相互&ldquo;接触&rdquo;，但没有相互重叠。</li>

</ol>



<p><strong>示例 1:</strong></p>



<pre>

<strong>输入:</strong> [ [1,2], [2,3], [3,4], [1,3] ]



<strong>输出:</strong> 1



<strong>解释:</strong> 移除 [1,3] 后，剩下的区间没有重叠。

</pre>



<p><strong>示例 2:</strong></p>



<pre>

<strong>输入:</strong> [ [1,2], [1,2], [1,2] ]



<strong>输出:</strong> 2



<strong>解释:</strong> 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

</pre>



<p><strong>示例 3:</strong></p>



<pre>

<strong>输入:</strong> [ [1,2], [2,3] ]



<strong>输出:</strong> 0



<strong>解释:</strong> 你不需要移除任何区间，因为它们已经是无重叠的了。

</pre>





 **难度**: Medium



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了75.22% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了20.87% 的用户

解题思路：
    贪心算法，排序后，前面的区间，起始均小于等于后面区间起始。
    若想删除最少的区间，只需保证每次保留末尾靠前的区间即可。

    对于两个区间[a1, a2], [b1, b2]共分三种情况：
        1.  存在交叉, 删除后一个区间
            a1,     a2
                b1,    b2

        2.  存在并集， 删除前一个区间
            a1,         a2
                b1, b2
        3.  无交叉， 不需要删除
            a1, a2
                b1, b2

            a1, a2
                    b1, b2

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        i = 0
        j = 1
        while i+j < len(intervals):
            # print(i, j, intervals[i], intervals[j+i], result)
            if intervals[i+j][0] < intervals[i][1] <= intervals[i+j][1]: # 存在交叉， 则跳过后一个区间，继续匹配
                result += 1
                j += 1
            elif intervals[i+j][1] <= intervals[i][1]:  # 后一个区间包含在当前区间内， 则以后一个区间继续匹配
                result += 1
                i = i + j
                j = 1
            else:   # 如果不存在交叉，则处理下一个区间
                i = i+j
                j = 1
        return result
</code></pre></div>
