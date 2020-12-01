Leetcode 1122. 数组的相对排序
<p>给你两个数组，<code>arr1</code> 和 <code>arr2</code>，</p>


<ul>

	<li><code>arr2</code> 中的元素各不相同</li>

	<li><code>arr2</code> 中的每个元素都出现在 <code>arr1</code> 中</li>

</ul>



<p>对 <code>arr1</code> 中的元素进行排序，使 <code>arr1</code> 中项的相对顺序和 <code>arr2</code> 中的相对顺序相同。未在 <code>arr2</code> 中出现过的元素需要按照升序放在 <code>arr1</code> 的末尾。</p>



<p> </p>



<p><strong>示例：</strong></p>



<pre>

<strong>输入：</strong>arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]

<strong>输出：</strong>[2,2,2,1,4,3,3,9,6,7,19]

</pre>



<p> </p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 <= arr1.length, arr2.length <= 1000</code></li>

	<li><code>0 <= arr1[i], arr2[i] <= 1000</code></li>

	<li><code>arr2</code> 中的元素 <code>arr2[i]</code> 各不相同</li>

	<li><code>arr2</code> 中的每个元素 <code>arr2[i]</code> 都出现在 <code>arr1</code> 中</li>

</ul>





 **难度**: Easy



 **标签**: 排序、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.13% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了66.55% 的用户

解题思路：
    自定义排序
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_dic = {a:i for i, a in enumerate(arr2)}    # 将arr2 按 元素:顺序 组成字典
        arr1.sort(key=lambda x:sort_dic[x] if x in sort_dic else len(arr2)+x) # 如果在字典中，则按照字典顺序排序，如不在字典中，则按照x本来的值排序
        return arr1
</code></pre></div>
