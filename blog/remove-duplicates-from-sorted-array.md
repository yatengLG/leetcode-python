Leetcode 26. 删除排序数组中的重复项
<p>给定一个排序数组，你需要在<strong><a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a></strong> 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。</p>


<p>不要使用额外的数组空间，你必须在 <strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组 </strong>并在使用 O(1) 额外空间的条件下完成。</p>



<p>&nbsp;</p>



<p><strong>示例&nbsp;1:</strong></p>



<pre>给定数组 <em>nums</em> = <strong>[1,1,2]</strong>, 



函数应该返回新的长度 <strong>2</strong>, 并且原数组 <em>nums </em>的前两个元素被修改为 <strong><code>1</code></strong>, <strong><code>2</code></strong>。 



你不需要考虑数组中超出新长度后面的元素。</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre>给定<em> nums </em>= <strong>[0,0,1,1,1,2,2,3,3,4]</strong>,



函数应该返回新的长度 <strong>5</strong>, 并且原数组 <em>nums </em>的前五个元素被修改为 <strong><code>0</code></strong>, <strong><code>1</code></strong>, <strong><code>2</code></strong>, <strong><code>3</code></strong>, <strong><code>4</code></strong>。



你不需要考虑数组中超出新长度后面的元素。

</pre>



<p>&nbsp;</p>



<p><strong>说明:</strong></p>



<p>为什么返回数值是整数，但输出的答案是数组呢?</p>



<p>请注意，输入数组是以<strong>「引用」</strong>方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。</p>



<p>你可以想象内部操作如下:</p>



<pre>// <strong>nums</strong> 是以&ldquo;引用&rdquo;方式传递的。也就是说，不对实参做任何拷贝

int len = removeDuplicates(nums);



// 在函数里修改输入数组对于调用者是可见的。

// 根据你的函数返回的长度, 它会打印出数组中<strong>该长度范围内</strong>的所有元素。

for (int i = 0; i &lt; len; i++) {

&nbsp; &nbsp; print(nums[i]);

}

</pre>





 **难度**: Easy



 **标签**: 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了27.10% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了34.72% 的用户

解题思路：
    循环遍历，如果相等，则调用del删除元素
    这个实际与题意不符，题中所述：返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 不需要考虑数组中超出新长度后面的元素
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1
        return len(nums)


"""
执行用时：40 ms, 在所有 Python3 提交中击败了96.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了48.50% 的用户

解题思路：
    循环，使用index记录不重复的元素个数，依次遍历列表
    重复则跳过，不重复则将当前index元素替换为不重复元素
    最终，前index个元素均不重复即可，后面元素不予考虑
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        record = None
        index = 0
        for i, value in enumerate(nums):
            if value == record:
                pass
            else:
                record = value
                nums[index] = record
                index += 1
        return index

</code></pre></div>
