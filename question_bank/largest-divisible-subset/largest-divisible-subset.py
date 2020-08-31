# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：376 ms, 在所有 Python3 提交中击败了74.29% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了57.14% 的用户

解题思路：
    动态规划

    例：
            i
        1,  2,  3,  4,  6,  7,  8,  9,  12
        0   1   1   2   2   1   3   2   3

        对于每一个数字，均需要与比其小的数进行相除。
    具体实现见代码注释
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        dp = [0 for _ in range(n)]  # 用于记录当前数字前的最大整除子集长度
        results = [[num]for num in nums]    # 用于记录对应的最大整除子集
        index, max_ = 0, 0  # 用于记录最大整除子集对应的下标
        for i in range(1, n):   # 遍历nums
            result=[]
            for j in range(0,i):
                if nums[i] % nums[j] == 0 and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1         # 更新最大整除子集长度
                    result = results[j]
            results[i] = result+[nums[i]]   # 更新最大整除子集
            if dp[i] > max_:                # # 更新最大整除子集对应下标
                max_ = dp[i]
                index = i
        return results[index]