Leetcode 406. 根据身高重建队列
<p>假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对 <code>(h, k)</code> 表示，其中 <code>h</code> 是这个人的身高，<code>k</code> 是应该排在这个人前面且身高大于或等于 <code>h</code> 的人数。 例如：[5,2] 表示前面应该有 2 个身高大于等于 5 的人，而 [5,0] 表示前面不应该存在身高大于等于 5 的人。</p>


<p>编写一个算法，根据每个人的身高 <code>h</code> 重建这个队列，使之满足每个整数对 <code>(h, k)</code> 中对人数 <code>k</code> 的要求。</p>



<ul>

</ul>



<p><strong>示例：</strong></p>



<pre>

<strong>输入：</strong>[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

<strong>输出：</strong>[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]</pre>



<p> </p>



<p><strong>提示：</strong></p>



<ul>

	<li>总人数少于 1100 人。</li>

</ul>





 **难度**: Medium



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了98.07% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了74.27% 的用户

解题思路：
    [h, k] 表示，其中 h 是这个人的身高，k 是应该排在这个人前面且身高大于或等于 h 的人数

        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    先进行排序，按照h从高到低，k从小到大排列
        [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
    然后依次插入结果即可
    后插入的必定比先插入的个子低，所以，此时按照k插入即可
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1])) # 按个头从高到低，前面人数从少到多排序
        result = []
        for p in people:
            result.insert(p[1], p)  # 依次按照前面高个子数量插入列表
        return result
</code></pre></div>
