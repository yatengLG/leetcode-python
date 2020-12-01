Leetcode 1356. 根据数字二进制下 1 的数目排序
<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;。请你将数组中的元素按照其二进制表示中数字 <strong>1</strong> 的数目升序排序。</p>


<p>如果存在多个数字二进制中&nbsp;<strong>1</strong>&nbsp;的数目相同，则必须将它们按照数值大小升序排列。</p>



<p>请你返回排序后的数组。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [0,1,2,3,4,5,6,7,8]

<strong>输出：</strong>[0,1,2,4,8,3,5,6,7]

<strong>解释：</strong>[0] 是唯一一个有 0 个 1 的数。

[1,2,4,8] 都有 1 个 1 。

[3,5,6] 有 2 个 1 。

[7] 有 3 个 1 。

按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [1024,512,256,128,64,32,16,8,4,2,1]

<strong>输出：</strong>[1,2,4,8,16,32,64,128,256,512,1024]

<strong>解释：</strong>数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>arr = [10000,10000]

<strong>输出：</strong>[10000,10000]

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>arr = [2,3,5,7,11,13,17,19]

<strong>输出：</strong>[2,3,5,17,7,11,13,19]

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入：</strong>arr = [10,100,1000,10000]

<strong>输出：</strong>[10,100,10000,1000]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= arr.length &lt;= 500</code></li>

	<li><code>0 &lt;= arr[i] &lt;= 10^4</code></li>

</ul>





 **难度**: Easy



 **标签**: 排序、 位运算、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了26.50% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了25.81% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        record = dict() # {int:list} 出现int次1 的各数组成的列表
        for i in range(len(arr)):
            a = arr[i]
            num = 0
            while a > 0:
                num += (a == a | 1) # 看最后位是否是1
                a = a >> 1  # 右移
            if num not in record:   # 存入字段
                record[num] = [arr[i]]
            else:
                record[num].append(arr[i])
        result = []
        keys_sort = list(record.keys()) # 对字典key进行排序
        keys_sort.sort()
        for key in keys_sort:
            record[key].sort()
            result.extend(record[key])
        return result

"""
执行用时：68 ms, 在所有 Python3 提交中击败了20.30% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了22.39% 的用户

解题思路：
    将数转换为二进制，然后统计出现的1.然后排序
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x:(bin(x).count('1'), x))
        return arr</code></pre></div>
