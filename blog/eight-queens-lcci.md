Leetcode 面试题 08.12. 八皇后
<p>设计一种算法，打印 N 皇后在 N &times; N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的&ldquo;对角线&rdquo;指的是所有的对角线，不只是平分整个棋盘的那两条对角线。</p>


<p><strong>注意：</strong>本题相对原题做了扩展</p>



<p><strong>示例:</strong></p>



<pre><strong> 输入</strong>：4

<strong> 输出</strong>：[[&quot;.Q..&quot;,&quot;...Q&quot;,&quot;Q...&quot;,&quot;..Q.&quot;],[&quot;..Q.&quot;,&quot;Q...&quot;,&quot;...Q&quot;,&quot;.Q..&quot;]]

<strong> 解释</strong>: 4 皇后问题存在如下两个不同的解法。

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





 **难度**: Hard



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：60 ms, 在所有 Python3 提交中击败了88.57% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了22.64% 的用户

解题思路：
    回溯
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_record = []     # 列记录
        dia1_record = []    # 对角线1记录
        dia2_record = []    # 对角线2记录
        result = []
        def backtrack(r, current):
            if r >= n:  # 如果最后一行也放置完成，则添加到最终结果中
                board = [['.' for _ in range(n)] for _ in range(n)]
                for r,c in current:
                    board[r][c] = 'Q'
                    board[r] = ''.join(board[r])
                result.append(board[:])
                return
            for c in range(n):  # 在本行中依次在每一列上进行放置
                if c not in col_record and r-c not in dia1_record and r+c not in dia2_record:   # 查看是否已经放置过
                    col_record.append(c)
                    dia1_record.append(r-c)
                    dia2_record.append(r+c)
                    backtrack(r+1, current+[(r, c)])    # 放置下一行
                    col_record.pop()
                    dia1_record.pop()
                    dia2_record.pop()
        backtrack(0, [])
        return result
</code></pre></div>
