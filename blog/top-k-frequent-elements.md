Leetcode 347. 前 K 个高频元素
<p>给定一个非空的整数数组，返回其中出现频率前&nbsp;<strong><em>k&nbsp;</em></strong>高的元素。</p>


<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入: </strong>nums = [1,1,1,2,2,3], k = 2

<strong>输出: </strong>[1,2]

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入: </strong>nums = [1], k = 1

<strong>输出: </strong>[1]</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>你可以假设给定的&nbsp;<em>k&nbsp;</em>总是合理的，且 1 &le; k &le; 数组中不相同的元素的个数。</li>

	<li>你的算法的时间复杂度<strong>必须</strong>优于 O(<em>n</em> log <em>n</em>) ,&nbsp;<em>n&nbsp;</em>是数组的大小。</li>

	<li>题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。</li>

	<li>你可以按任意顺序返回答案。</li>

</ul>





 **难度**: Medium



 **标签**: 堆、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了98.35% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了83.91% 的用户

解题思路：
    先遍历整个列表，统计每个数字出现的次数
    然后翻转字典，统计出现次数，并排序，从翻转字典中查找对应的数字
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            if num not in record:
                record[num] = 1
            else:
                record[num] += 1

        record_ = {}
        for key, value in record.items():
            if value not in record_:
                record_[value] = [key]
            else:
                record_[value].append(key)

        value = list(record.values())
        value.sort(reverse=True)

        result = []
        if k == 1:
            result.extend(record_[value[0]])
            return result

        for k in set(value[:k]):
            result.extend(record_[k])
        return result
</code></pre></div>
