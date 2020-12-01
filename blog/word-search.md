Leetcode 79. 单词搜索
<p>给定一个二维网格和一个单词，找出该单词是否存在于网格中。</p>


<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中&ldquo;相邻&rdquo;单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>



<p>&nbsp;</p>



<p><strong>示例:</strong></p>



<pre>board =

[

  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],

  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],

  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]

]



给定 word = &quot;<strong>ABCCED</strong>&quot;, 返回 <strong>true</strong>

给定 word = &quot;<strong>SEE</strong>&quot;, 返回 <strong>true</strong>

给定 word = &quot;<strong>ABCB</strong>&quot;, 返回 <strong>false</strong></pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>board</code> 和 <code>word</code> 中只包含大写和小写英文字母。</li>

	<li><code>1 &lt;= board.length &lt;= 200</code></li>

	<li><code>1 &lt;= board[i].length &lt;= 200</code></li>

	<li><code>1 &lt;= word.length &lt;= 10^3</code></li>

</ul>





 **难度**: Medium



 **标签**: 数组、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：352 ms, 在所有 Python3 提交中击败了15.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了38.04% 的用户

解题思路：
    回溯
    依次以board上每个点作为起始点，与word中字母进行匹配
    若匹配，则寻找board当前点四周，是否与word中下一个相匹配的，若找不到，则回溯
    具体事项见代码注释
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w, n = len(board), len(board[0]), len(word)  # 网格宽高，与word长度
        if h*w < n:
            return False
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 四周坐标向量
        def backtrack(i, j, k, current):    #  网格第i行j列，word第k个字符，当前已匹配的网格
            if len(current) == n:   # 若当前匹配以匹配所有字符，返回true
                return True
            if not (-1 < i < h and -1 < j < w): # 网格索引限制
                return False
            if board[i][j] == word[k]:  # 当前网格字符与word[k]匹配
                current.append((i, j))  # 将当前网格坐标添加到已匹配队列中
                for direction in directions:    # 向四周延伸
                    new_i, new_j = i+direction[0], j+direction[1]
                    if (new_i, new_j) not in current :
                        if backtrack(new_i, new_j, k+1, current):   # 对当前网格四周匹配下一个word中字符
                            return True
                current.pop()   # 若四周不匹配，则回溯

        for i in range(h):
            for j in range(w):
                if backtrack(i, j, 0, []):
                    return True
        return False


"""
执行用时：304 ms, 在所有 Python3 提交中击败了25.04% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了75.00% 的用户

解题思路：
    回溯
    更改了部分逻辑
    现在从一个已经匹配的字符开始向四周寻找
    自行打印current,与上例进行比较即可查看出差异
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w, n = len(board), len(board[0]), len(word)  # 网格宽高，与word长度
        if h*w < n:
            return False
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 四周坐标向量

        def backtrack(i, j, k, current):    #  网格第i行j列，word第k个字符，当前已匹配的网格
            # print(i, j, k, current)
            if len(current) == n:   # 若当前匹配以匹配所有字符，返回true
                return True

            for direction in directions:    # 向四周延伸
                new_i, new_j = i+direction[0], j+direction[1]
                if -1 < new_i < h and -1 < new_j < w and board[new_i][new_j] == word[k] and (new_i, new_j) not in current :
                    current.append((new_i, new_j))
                    if backtrack(new_i, new_j, k+1, current):   # 对当前网格四周匹配下一个word中字符
                        return True
            current.pop()   # 若四周不匹配，则回溯


        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1, [(i, j)]):
                        return True
        return False

"""
执行用时：224 ms, 在所有 Python3 提交中击败了73.37% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了51.48% 的用户

解题思路：
    回溯
    将列表改换为字典
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h, w, n = len(board), len(board[0]), len(word)  # 网格宽高，与word长度
        if h*w < n:
            return False
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 四周坐标向量
        current = {}
        def backtrack(i, j, k, ):    #  网格第i行j列，word第k个字符，当前已匹配的网格
            # print(i, j, k, current)
            if len(current) == n:   # 若当前匹配以匹配所有字符，返回true
                return True

            for direction in directions:    # 向四周延伸
                new_i, new_j = i+direction[0], j+direction[1]
                if -1 < new_i < h and -1 < new_j < w and board[new_i][new_j] == word[k] and (new_i, new_j) not in current:
                    current[(new_i, new_j)] = 0
                    if backtrack(new_i, new_j, k+1):   # 对当前网格四周匹配下一个word中字符
                        return True
            del current[(i, j)]   # 若四周不匹配，则回溯

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    current[(i, j)] = 0
                    if backtrack(i, j, 1):
                        return True
        return False
</code></pre></div>
