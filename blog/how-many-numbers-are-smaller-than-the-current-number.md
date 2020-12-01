Leetcode 1365. 有多少小于当前数字的数字
<p>给你一个数组&nbsp;<code>nums</code>，对于其中每个元素&nbsp;<code>nums[i]</code>，请你统计数组中比它小的所有数字的数目。</p>


<p>换而言之，对于每个&nbsp;<code>nums[i]</code>&nbsp;你必须计算出有效的&nbsp;<code>j</code>&nbsp;的数量，其中 <code>j</code> 满足&nbsp;<code>j != i</code> <strong>且</strong> <code>nums[j] &lt; nums[i]</code>&nbsp;。</p>



<p>以数组形式返回答案。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>nums = [8,1,2,2,3]

<strong>输出：</strong>[4,0,1,1,3]

<strong>解释：</strong> 

对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 

对于 nums[1]=1 不存在比它小的数字。

对于 nums[2]=2 存在一个比它小的数字：（1）。 

对于 nums[3]=2 存在一个比它小的数字：（1）。 

对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>nums = [6,5,4,8]

<strong>输出：</strong>[2,1,0,3]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>nums = [7,7,7,7]

<strong>输出：</strong>[0,0,0,0]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>2 &lt;= nums.length &lt;= 500</code></li>

	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>

</ul>





 **难度**: Easy



 **标签**: 数组、 哈希表、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了99.89% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.09% 的用户

解题思路：
    统计num出现的次数
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        record1, record2 = [0] * 101, [0] * 101

        for num in nums:
            record1[num] += 1   # 统计每个数出现的次数

        for i in range(1, 101):
            record2[i] = record1[i-1] + record2[i-1]    # 计算比当前数小的数的个数

        result = []
        for num in nums:
            result += [record2[num]]
        return result


"""
执行用时：112 ms, 在所有 Python3 提交中击败了50.42% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了8.85% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        record = {} # 统计比当前数小的数个数
        record_n = defaultdict(int) # 统计当前数的出现次数
        for num in nums:
            if num in record:
                record_n[num] += 1
                continue
            record[num] = 0

            for r in record:
                if r > num:
                    record[r] += 1
                elif r < num:
                    record[num] += 1

        result = []
        for num in nums:
            n = record[num] # 最终结果，小于当前数的个数+每个小于当前数的数的出现次数
            for rn in record_n:
                if rn < num:
                    n += record_n[rn]
            result += [n]
        return result</code></pre></div>
