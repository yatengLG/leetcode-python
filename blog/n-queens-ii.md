Leetcode 52. N皇后 II
<p><em>n&nbsp;</em>皇后问题研究的是如何将 <em>n</em>&nbsp;个皇后放置在 <em>n</em>&times;<em>n</em> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>


<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png" style="height: 276px; width: 258px;"></p>



<p><small>上图为 8 皇后问题的一种解法。</small></p>



<p>给定一个整数 <em>n</em>，返回 <em>n</em> 皇后不同的解决方案的数量。</p>



<p><strong>示例:</strong></p>



<pre><strong>输入:</strong> 4

<strong>输出:</strong> 2

<strong>解释:</strong> 4 皇后问题存在如下两个不同的解法。

[

&nbsp;[&quot;.Q..&quot;, &nbsp;// 解法 1

&nbsp; &quot;...Q&quot;,

&nbsp; &quot;Q...&quot;,

&nbsp; &quot;..Q.&quot;],



&nbsp;[&quot;..Q.&quot;, &nbsp;// 解法 2

&nbsp; &quot;Q...&quot;,

&nbsp; &quot;...Q&quot;,

&nbsp; &quot;.Q..&quot;]

]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><strong>皇后</strong>，是<a href="https://baike.baidu.com/item/%E5%9B%BD%E9%99%85%E8%B1%A1%E6%A3%8B" target="_blank">国际象棋</a>中的棋子，意味着<a href="https://baike.baidu.com/item/%E5%9B%BD%E7%8E%8B" target="_blank">国王</a>的妻子。皇后只做一件事，那就是&ldquo;<a href="https://baike.baidu.com/item/%E5%90%83%E5%AD%90" target="_blank">吃子</a>&rdquo;。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N-1 步，可进可退。（引用自 <a href="https://baike.baidu.com/item/%E7%9A%87%E5%90%8E/15860305?fr=aladdin">百度百科 - 皇后</a> ）</li>

</ul>





 **难度**: Hard



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：56 ms, 在所有 Python3 提交中击败了80.87% 的用户
内存消耗：13.9 MB, 在所有 Python3 提交中击败了8.27% 的用户

解题思路：
    回溯
    同N皇后解题思路，但由于只需要计算题解数量
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        col = []
        obl1 = []
        obl2 = []
        result = [0]

        def backtrack(i:int, current:int):
            if current == n:
                result[0] += 1
                return

            for j in range(n):
                if j not in col and j-i not in obl1 and j+i not in obl2:
                    col.append(j)
                    obl1.append(j-i)
                    obl2.append(j+i)
                    current += 1
                    backtrack(i+1, current)
                    current -= 1
                    col.pop()
                    obl1.pop()
                    obl2.pop()

        backtrack(0, 0)
        return result[0]</code></pre></div>
