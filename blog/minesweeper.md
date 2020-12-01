Leetcode 529. 扫雷游戏
<p>让我们一起来玩扫雷游戏！</p>


<p>给定一个代表游戏板的二维字符矩阵。&nbsp;<strong>&#39;M&#39;</strong>&nbsp;代表一个<strong>未挖出的</strong>地雷，<strong>&#39;E&#39;</strong>&nbsp;代表一个<strong>未挖出的</strong>空方块，<strong>&#39;B&#39;&nbsp;</strong>代表没有相邻（上，下，左，右，和所有4个对角线）地雷的<strong>已挖出的</strong>空白方块，<strong>数字</strong>（&#39;1&#39; 到 &#39;8&#39;）表示有多少地雷与这块<strong>已挖出的</strong>方块相邻，<strong>&#39;X&#39;</strong>&nbsp;则表示一个<strong>已挖出的</strong>地雷。</p>



<p>现在给出在所有<strong>未挖出的</strong>方块中（&#39;M&#39;或者&#39;E&#39;）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：</p>



<ol>

	<li>如果一个地雷（&#39;M&#39;）被挖出，游戏就结束了- 把它改为&nbsp;<strong>&#39;X&#39;</strong>。</li>

	<li>如果一个<strong>没有相邻地雷</strong>的空方块（&#39;E&#39;）被挖出，修改它为（&#39;B&#39;），并且所有和其相邻的<strong>未挖出</strong>方块都应该被递归地揭露。</li>

	<li>如果一个<strong>至少与一个地雷相邻</strong>的空方块（&#39;E&#39;）被挖出，修改它为数字（&#39;1&#39;到&#39;8&#39;），表示相邻地雷的数量。</li>

	<li>如果在此次点击中，若无更多方块可被揭露，则返回面板。</li>

</ol>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入:</strong> 



[[&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;],

 [&#39;E&#39;, &#39;E&#39;, &#39;M&#39;, &#39;E&#39;, &#39;E&#39;],

 [&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;],

 [&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;]]



Click : [3,0]



<strong>输出:</strong> 



[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;M&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]



<strong>解释:</strong>

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/minesweeper_example_1.png" style="width: 100%;">

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入:</strong> 



[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;M&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]



Click : [1,2]



<strong>输出:</strong> 



[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;X&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],

 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]



<strong>解释:</strong>

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/minesweeper_example_2.png" style="width: 100%;">

</pre>



<p>&nbsp;</p>



<p><strong>注意：</strong></p>



<ol>

	<li>输入矩阵的宽和高的范围为 [1,50]。</li>

	<li>点击的位置只能是未被挖出的方块 (&#39;M&#39; 或者 &#39;E&#39;)，这也意味着面板至少包含一个可点击的方块。</li>

	<li>输入面板不会是游戏结束的状态（即有地雷已被挖出）。</li>

	<li>简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。</li>

</ol>





 **难度**: Medium



 **标签**: 深度优先搜索、 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：248 ms, 在所有 Python3 提交中击败了36.27% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了10.36% 的用户

解题思路：
    模拟点击
    当发生点击操作时，有三种情况：
        1. 点击到'M'， 也就是点击到雷，此时，把雷 改成'X'， 返回即可
        2. 点击到'E'，也即是未点到雷时，需要遍历周围情况：
            3. 是否与雷相邻，，如果相邻，则把当前'E'， 改成周围雷的数量
            4. 如果不相邻，则改为'B'，且开始遍历周围其他块
    具体实现见代码备注
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        directions = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1] ]    # 八个方位

        def f(i, j):    # 定义一个点击函数，用于遍历
            record = [] # 记录周围需要点击的'E'的坐标
            mines = 0   # 记录当前坐标周围雷的数量
            for direction in directions:    # 八个方位，挨着遍历
                new_i, new_j = i + direction[0], j+direction[1]
                if 0 <= new_i < m and 0 <= new_j < n:   # 如果越界，则忽略
                    if board[new_i][new_j] == 'M':      # 周围有雷， 雷数量+1
                        mines += 1
                    elif board[new_i][new_j] == 'E':    # 周围不是雷，将这个坐标记录下来
                        record.append([new_i, new_j])

            if mines == 0:  # 如果雷的数量是0，则为'B', 且需要遍历周围其他不是雷的区域
                board[i][j] = 'B'
                for new_i, new_j in record: # 遍历周围其他区域
                    f(new_i, new_j)
            else:
                board[i][j] = str(mines)    # 如果存在雷，则将该坐标 改为雷的数量

        i, j = click
        if board[i][j] == 'M':  # 第一次点击，是雷，则需要改为X，返回即可
            board[i][j] = 'X'
            return board

        elif board[i][j] == 'E':    # 不是雷，则需要以当前坐标为中心开始遍历周围点
            f(i, j)

        return board
</code></pre></div>
