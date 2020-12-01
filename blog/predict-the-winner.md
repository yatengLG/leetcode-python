Leetcode 486. 预测赢家
<p>给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，&hellip;&hellip; 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。</p>


<p>给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[1, 5, 2]

<strong>输出：</strong>False

<strong>解释：</strong>一开始，玩家1可以从1和2中进行选择。

如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。

所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。

因此，玩家 1 永远不会成为赢家，返回 False 。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[1, 5, 233, 7]

<strong>输出：</strong>True

<strong>解释：</strong>玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。

     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>1 &lt;= 给定的数组长度&nbsp;&lt;= 20.</li>

	<li>数组里所有分数都为非负数且不会大于 10000000 。</li>

	<li>如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。</li>

</ul>





 **难度**: Medium



 **标签**: 极小化极大、 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1828 ms, 在所有 Python3 提交中击败了9.51% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了57.59% 的用户

解题思路：
    递归。 思路参考了https://leetcode-cn.com/problems/predict-the-winner/solution/xie-gei-suan-fa-ru-men-zhe-wo-zi-ji-de-pythonti-ji/

    主要记录下自己学习到的东西
    对于列表的递归，使用指针是更方便的
    具体实现见代码注释
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def choose(l, r, reverse):  # 通过左右指针来表示取左侧还是右侧数字， 通过reverse表示轮谁取数字， 1为玩家一，-1为玩家二
            if l == r:              # 省单个元素，直接取
                return reverse * nums[l]
            get_left = reverse * nums[l] + choose(l+1, r, -reverse)     # 取左侧数字， 左指移动，玩家切换
            get_right = reverse * nums[r] + choose(l, r-1, -reverse)    # 取右侧数字，右指针移动，玩家切换
            if reverse == 1:                                            # 如果玩家一取，则返回分数最大值， 玩家二取，则返回分数最小值. 目的是使最终的玩家一分数尽可能大
                return max(get_left, get_right)
            else:
                return min(get_left, get_right)
        n = len(nums)
        if n % 2 == 0:  # 偶数个数值，则玩家一二均可取到某一值，可能赢
            return True
        else:
            if choose(0, n-1, 1) >= 0:  # 最终分数为玩家一尽可能大的分数，如果大于0，则玩家一可能赢
                return True
            else:
                return False


"""
执行用时：28 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了81.58% 的用户

解题思路：
    动态规划
    例：
         i  j
        [1, 2, 3, 4, 5]
        
            1   2   3   4   5
        1   1   1   2   2   3
        2   0   2   1   3   2
        3   0   0   3   1   4
        4   0   0   0   4   1
        5   0   0   0   0   5
    
    其中 i,j为指针，指向 字符串
    dp[i][j] 表示只有 nums[i]~nums[j]时的分数差
    则 dp[i][i] = nums[i] 只有一个数字时，玩家一先拿，则 分数差为nums[i]
    则 dp[i][j] = max(nums[j]-dp[i][j-1], num[i]-dp[i+1][j])
        i~j 的差值，等于 nums[i] 与 i+1～j的分数差，  与 nums[j] 与 i~j-1 的分数差的 最大值。
            因为玩家一会先选，则必然从头尾拿， 
                nums[i]- dp[i+1][j] 表示从左侧拿
                nums[j]- dp[i][j-1] 表示从右侧拿
"""


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        if dp[0][-1] >= 0:
            return True
        else:
            return False
</code></pre></div>
