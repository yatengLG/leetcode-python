Leetcode 621. 任务调度器
<p>给你一个用字符数组 <code>tasks</code> 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。</p>


<p>然而，两个<strong> 相同种类</strong> 的任务之间必须有长度为整数<strong> </strong><code>n</code><strong> </strong>的冷却时间，因此至少有连续 <code>n</code> 个单位时间内 CPU 在执行不同的任务，或者在待命状态。</p>



<p>你需要计算完成所有任务所需要的<strong> 最短时间</strong> 。</p>



<p> </p>



<p><strong>示例 1：</strong></p>



<pre>

<strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 2

<strong>输出：</strong>8

<strong>解释：</strong>A -> B -> (待命) -> A -> B -> (待命) -> A -> B

     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 </pre>



<p><strong>示例 2：</strong></p>



<pre>

<strong>输入：</strong>tasks = ["A","A","A","B","B","B"], n = 0

<strong>输出：</strong>6

<strong>解释：</strong>在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0

["A","A","A","B","B","B"]

["A","B","A","B","A","B"]

["B","B","B","A","A","A"]

...

诸如此类

</pre>



<p><strong>示例 3：</strong></p>



<pre>

<strong>输入：</strong>tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2

<strong>输出：</strong>16

<strong>解释：</strong>一种可能的解决方案是：

     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A

</pre>



<p> </p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 <= task.length <= 10<sup>4</sup></code></li>

	<li><code>tasks[i]</code> 是大写英文字母</li>

	<li><code>n</code> 的取值范围为 <code>[0, 100]</code></li>

</ul>





 **难度**: Medium



 **标签**: 贪心算法、 队列、 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms, 在所有 Python3 提交中击败了98.06% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了18.73% 的用户

解题思路：贪心算法
    tasks = ["A","A","A","B","B","B","C","C","C","D","E"], n = 2, leastInterval = 16

        A   B   C   D
        A   B   C   E
        A   B   C

    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2, leastInterval = 16

        A   B   C
        A   D   E
        A   F   G
        A   _   _
        A   _   _
        A
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)  # 统计每个字符出现的次数
        h = max([v for _,v in count.items()])   # 选最大的作为矩形高
        w = len([v for _,v in count.items() if v == h]) # 将出现次数等于h的元素先放进矩阵，此时，矩阵宽w
        ew = max(math.ceil((len(tasks) - h*w)/h), n-w+1)    # 剩余字符放入矩阵，所需的额外宽ew

        if n - w + 1 > (len(tasks) - h * w) / h:    # 若剩余字符未放满ew*h
            num = h * w + max((len(tasks) - h * w), ew * (h - 1))
        else:                                       # 若剩余字符超出了ew*h, h * w + len(tasks) - h * w
            num = len(tasks)
        return num

</code></pre></div>
