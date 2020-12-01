Leetcode 37. 解数独
<p>编写一个程序，通过已填充的空格来解决数独问题。</p>


<p>一个数独的解法需<strong>遵循如下规则</strong>：</p>



<ol>

	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>

	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>

	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。</li>

</ol>



<p>空白格用&nbsp;<code>&#39;.&#39;</code>&nbsp;表示。</p>



<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png"></p>



<p><small>一个数独。</small></p>



<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png"></p>



<p><small>答案被标成红色。</small></p>



<p><strong>Note:</strong></p>



<ul>

	<li>给定的数独序列只包含数字&nbsp;<code>1-9</code>&nbsp;和字符&nbsp;<code>&#39;.&#39;</code>&nbsp;。</li>

	<li>你可以假设给定的数独只有唯一解。</li>

	<li>给定数独永远是&nbsp;<code>9x9</code>&nbsp;形式的。</li>

</ul>





 **难度**: Hard



 **标签**: 哈希表、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：196 ms, 在所有 Python3 提交中击败了62.91% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了98.31% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        w, h = len(board), len(board[0])    # 数独的长宽， 实际上 都是9
        rows_record = [[] for _ in range(w)]    # 用来记录 每一行 用过的数字     9行
        cols_record = [[] for _ in range(h)]    # 用来记录每一列用过的数字       9列
        blocks_record = [[] for _ in range(w)]  # 用来记录每一个方块用过的数字    9个方块
        unuse_coord = []                        # 用来记录需要填写的空的坐标
        results = []                            # 最终填写结果，（r,c,num） 行、列、数

        # 读取棋盘信息，填写上述表
        for i, nums in enumerate(board):
            for j, num in enumerate(nums):
                now = board[i][j]
                if now == '.':
                    unuse_coord.append((i, j))
                else:
                    rows_record[i].append(now)
                    cols_record[j].append(now)
                    blocks_record[j//3 + i//3*3].append(now)

        def backtrack(i, used): # 未填写空的下标，填写过的信息列表

            if i >= len(unuse_coord):   # 如果都填完了，则将当前填写方式加入到最终结果中
                results.append(used.copy())
                return
            r, c  = unuse_coord[i]      # 当前填写的空的坐标。 行 列
            for num in '123456789':     # 用数字循环去试这个空

                if num not in rows_record[r] and num not in cols_record[c] and num not in blocks_record[c//3 + r//3*3]: # 填写检查
                    rows_record[r].append(num)  # 将当前数字加入到 行、列、块记录中，表明已使用
                    cols_record[c].append(num)
                    blocks_record[c//3 + r//3*3].append(num)
                    used.append((r,c,num))  # 将当前数字加入填写信息中
                    backtrack(i+1, used)    # 填下一个空

                    # 回溯
                    rows_record[r].pop()
                    cols_record[c].pop()
                    blocks_record[c // 3 + r // 3 * 3].pop()
                    used.pop()

        backtrack(0, [])

        result = results[0] # 这里写法会获得多个答案（如果存在多个答案），题中只要求一个

        # 将答案写入棋盘
        for coord in result:
            r, c, num = coord
            board[r][c] = num

</code></pre></div>
