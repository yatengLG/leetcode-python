Leetcode 845. 数组中的最长山脉
<p>我们把数组 A 中符合下列属性的任意连续子数组 B 称为 &ldquo;<em>山脉&rdquo;</em>：</p>


<ul>

	<li><code>B.length &gt;= 3</code></li>

	<li>存在 <code>0 &lt; i&nbsp;&lt; B.length - 1</code> 使得 <code>B[0] &lt; B[1] &lt; ... B[i-1] &lt; B[i] &gt; B[i+1] &gt; ... &gt; B[B.length - 1]</code></li>

</ul>



<p>（注意：B 可以是 A 的任意子数组，包括整个数组 A。）</p>



<p>给出一个整数数组 <code>A</code>，返回最长 <em>&ldquo;山脉&rdquo;</em>&nbsp;的长度。</p>



<p>如果不含有 &ldquo;<em>山脉&rdquo;&nbsp;</em>则返回 <code>0</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[2,1,4,7,3,2,5]

<strong>输出：</strong>5

<strong>解释：</strong>最长的 &ldquo;山脉&rdquo; 是 [1,4,7,3,2]，长度为 5。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[2,2,2]

<strong>输出：</strong>0

<strong>解释：</strong>不含 &ldquo;山脉&rdquo;。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>0 &lt;= A.length &lt;= 10000</code></li>

	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>

</ol>





 **难度**: Medium



 **标签**: 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了97.12% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了78.97% 的用户

解题思路：
    模拟提议，记录当前起伏状态，分析是否是山脉
    具体实现见代码注释
"""
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        s, p, l = 0, 0, 0   # 起始点，p指针，记录当前最长山脉长度
        up, down = False, False # 记录当前起伏状态
        while p < len(A)-1:
            if A[p] > A[p+1]: # 当前下降
                if up:  # 如果之前存在上升状态，则存在山脉，激活山脉的下降状态
                    down = True
                else:
                    s = p+1 # 否则，之前不存在山脉，将挪动起始点
            elif A[p] < A[p+1]:   # 当前上升
                if up == True and down == True: # 如果上升和下降状态激活， 则存在山脉，且山脉结束
                    l = max(l, p+1-s)   # 更新山脉长度
                    s = p   # 挪动起始点
                    down = False    # 重置起伏状态
                up = True
            else:   # 平地
                if up == True and down == True: # 如果之前存在山脉，则更新l
                    l = max(l, p+1 - s)
                up = False  # 重置起伏状态
                down = False
                s = p+1 # 挪动起始点
            p += 1
        if up == True and down == True: # 如果存在山脉，则更新l
            l = max(l, p+1 - s )
        return l
</code></pre></div>
