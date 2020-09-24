# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1732 ms, 在所有 Python3 提交中击败了12.27% 的用户
内存消耗：14 MB, 在所有 Python3 提交中击败了60.77% 的用户

解题思路：
    冒泡排序
    通过判断k与nums的长度，决定排序方向
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < 2:
            return nums[k-1]
        if k > n/2: # 如果 k>nums长度的一半
            for j in range(n-1):
                for i in range(n-1-j):
                    if nums[i] < nums[i + 1]:   # 从大到小拍,每次将最小值放到末尾
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                if j > n-k-1:
                    return nums[k-1]    # 取第k-1个则为第k个最大值
        else:       # 如果大于长度一半
            for j in range(n-1):
                for i in range(n-1-j):
                    if nums[i] > nums[i + 1]:   # 从小到大排,每次将最大值放到末尾
                        nums[i], nums[i + 1] = nums[i + 1], nums[i]
                if j > k-2:
                    return nums[-k] # 取第-k个即为第k个最大数