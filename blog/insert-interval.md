Leetcode 57. 插入区间
<p>给出一个<em>无重叠的 ，</em>按照区间起始端点排序的区间列表。</p>


<p>在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。</p>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1：</strong></p>



<pre><strong>输入：</strong>intervals = [[1,3],[6,9]], newInterval = [2,5]

<strong>输出：</strong>[[1,5],[6,9]]

</pre>



<p><strong>示例&nbsp;2：</strong></p>



<pre><strong>输入：</strong>intervals = <code>[[1,2],[3,5],[6,7],[8,10],[12,16]]</code>, newInterval = <code>[4,8]</code>

<strong>输出：</strong>[[1,2],[3,10],[12,16]]

<strong>解释：</strong>这是因为新的区间 <code>[4,8]</code> 与 <code>[3,5],[6,7],[8,10]</code>&nbsp;重叠。

</pre>



<p>&nbsp;</p>



<p><strong>注意：</strong>输入类型已在 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。</p>





 **难度**: Hard



 **标签**: 排序、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了93.88% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了10.79% 的用户

解题思路：
    模拟插入
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        start, end = newInterval[0], newInterval[1]
        if intervals == []: # 如果起始列表为空，则直接返回待插入列表
            return [newInterval]
        while i < len(intervals):
            if intervals[i][1] < start: # 待插入列表在当前列表元素右侧
                result.append(intervals[i]) # 直接插入当前元素
            elif end < intervals[i][0]: # 待插入列表在当前列表元素左侧，将待插入列表插入结果，以当前列表值更新待插入列表
                result.append([start, end])
                start, end = intervals[i]
            else:   # 当前列表与待插入列表存在交集，则更新待插入列表
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            i += 1
        result.append([start, end]) # 最后将待插入列表插入最终结果
        return result
</code></pre></div>
