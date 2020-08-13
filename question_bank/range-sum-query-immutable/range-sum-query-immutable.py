# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：88 ms, 在所有 Python3 提交中击败了95.50% 的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了17.70% 的用户

解题思路：
    动态规划
    ["NumArray","sumRange","sumRange","sumRange"]
    [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

    要求 (i, j)的和，可以看做求(0, j)-(0, i)，前j个的和-前i个的和。
    [-2, 0, 3, -5, 2, -1]
         i

    使用动态规划计算前i个的和
    dp[i] = dp[i-1] + nums[i]

"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n >= 1:
            self.dp = [[] for _ in range(self.n)]
            self.dp[0] = nums[0]
            for i in range(1, self.n):
                self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if self.n < 1:
            return None
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)