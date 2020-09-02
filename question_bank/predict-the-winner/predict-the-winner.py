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
