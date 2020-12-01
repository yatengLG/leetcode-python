Leetcode 89. 格雷编码
<p>格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。</p>


<p>给定一个代表编码总位数的非负整数<em> n</em>，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。</p>



<p>格雷编码序列必须以 0 开头。</p>



<p>&nbsp;</p>



<p><strong>示例 1:</strong></p>



<pre><strong>输入:</strong>&nbsp;2

<strong>输出:</strong>&nbsp;<code>[0,1,3,2]</code>

<strong>解释:</strong>

00 - 0

01 - 1

11 - 3

10 - 2



对于给定的&nbsp;<em>n</em>，其格雷编码序列并不唯一。

例如，<code>[0,2,3,1]</code>&nbsp;也是一个有效的格雷编码序列。



00 - 0

10 - 2

11 - 3

01 - 1</pre>



<p><strong>示例&nbsp;2:</strong></p>



<pre><strong>输入:</strong>&nbsp;0

<strong>输出:</strong>&nbsp;<code>[0]

<strong>解释:</strong> 我们定义</code>格雷编码序列必须以 0 开头。<code>

&nbsp;    给定</code>编码总位数为<code> <em>n</em> 的格雷编码序列，其长度为 2<sup>n</sup></code>。<code>当 <em>n</em> = 0 时，长度为 2<sup>0</sup> = 1。

&nbsp;    因此，当 <em>n</em> = 0 时，其格雷编码序列为 [0]。</code>

</pre>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：180 ms, 在所有 Python3 提交中击败了5.52% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.06% 的用户

解题思路：
    回溯
    回溯，直到找到一个满足条件的值
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        def backtrack(start:list, current:list):
            if len(current) >= 2**n:
                for b in current:
                    num = 0
                    for i, v in enumerate(b[::-1]):
                        num += v*2**i
                    result.append(num)
                return True

            for i in range(n):
                start_copy = start[:]
                start_copy[i] = 0 if start_copy[i]==1 else 1
                if start_copy not in current:
                    current.append(start_copy)
                    if backtrack(start_copy, current):
                        return True
                    current.pop()
        if backtrack([0]*n,[[0]*n]):
            return result
        else:
            return []


"""
执行用时：52 ms, 在所有 Python3 提交中击败了16.03% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了47.18% 的用户

解题思路：
    例： n = 4
    
            0   0   0   0   0000
                        1   0001
                    1   1   0011
                        0   0010
                1   1   0   0110
                        1   0111
                    0   1   0101
                        0   0100
            1   1   0   0   1100
                        1   1101
                    1   1   1111
                        0   1110
                0   1   0   1010
                        1   1011
                    0   1   1001
                        0   1000
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        strings = []
        for i in range(n):
            string=''
            reverse = False
            while len(string) < (2**n):
                if reverse:
                    string += '1' * int(2 ** i) + '0' * int(2 ** i)
                else:
                    string += '0' * int(2 ** i) + '1' * int(2 ** i)
                reverse = not reverse
            strings.append(string)

        result = [0 for _ in range(2**n)]
        for j, string in enumerate(strings):
            for i, s in enumerate(string):
                result[i] += int(s) * (2 ** j)
        return result

</code></pre></div>
