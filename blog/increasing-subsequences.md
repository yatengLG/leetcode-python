Leetcode 491. 递增子序列
<p>给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。</p>


<p><strong>示例:</strong></p>



<pre>

<strong>输入:</strong> [4, 6, 7, 7]

<strong>输出:</strong> [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]</pre>



<p><strong>说明:</strong></p>



<ol>

	<li>给定数组的长度不会超过15。</li>

	<li>数组中的整数范围是&nbsp;[-100,100]。</li>

	<li>给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。</li>

</ol>





 **难度**: Medium



 **标签**: 深度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：6804 ms, 在所有 Python3 提交中击败了25.89% 的用户
内存消耗：21.3 MB, 在所有 Python3 提交中击败了32.02% 的用户

解题思路：
    详见代码注释
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = []        # 用于保存最终结果
        for num in nums:    # 以每个数字作为起始，开始枚举所有组合
            results_ = []   # 用于保存中间结果，这里需要最后更新最终列表，所以在计算过程中需要保存一个中间值
            for result in results:  # 从保存的结果中，读取已经枚举过的结果
                if num >= result[-1]:   # 当前数字大于 结果中的最后一个，也就是最大值
                    record = result.copy()  # 因为是列表，所以需要使用copy
                    record.append(num)      # 将当前数组与结果 组成新的上升子序列
                    if record not in results and record not in results_:    # 判断重复
                        results_.append(record)
            results.extend(results_)    # 添加结果
            results.append([num])       # 需要将当前数字添加到结果中，这里是因为，初始结果是[]的，每次比较需要一个最初的比较对象
        results = [result for result in results if len(result) > 1] # 由于将单个数字也添加进了结果中，所以需要去掉
        return results


"""
执行用时：60 ms, 在所有 Python3 提交中击败了99.29% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了99.51% 的用户

解题思路：
    对上例进行优化。
    将上例中列表操作，更换为集合，省去了去重步骤。
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for num in nums:
            for result in list(results):
                if num >= result[-1]:
                    record = result + (num, )
                    results.add(record)
            results.add((num, ))
        results = [result for result in results if len(result) > 1]
        return results
</code></pre></div>
