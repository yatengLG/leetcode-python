# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：972 ms, 在所有 Python3 提交中击败了61.82% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了96.71% 的用户

解题思路：
    双指针法，固定一个值，然后双指针遍历其余值
    先对列表进行排序
    i 循环遍历列表，作为固定值
    l, r 作为左右指针，分别去遍历剩余值
    具体实现见代码注释
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        now = None  # 用于记录固定值，判断是否重复
        result = []
        for i in range(n):
            if nums[i] == now:  # 遇到重复的值，跳过
                continue
            now = nums[i]
            if nums[i] > 0: # 如果当前值大于0，则之后的和绝对大于0，跳出（因为已排序）
                break
            l, r = i+1, n-1 # 左右指针
            while l<r:  # 左指针小于右指针，循环
                if nums[i] + nums[l] + nums[r] == 0:    # 和为0
                    result.append([nums[i], nums[l], nums[r]])  # 添加进结果
                    while l < r and nums[l] == nums[l+1]:   # 左指针去重复
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   # 右指针去重复
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:     # 和<0， 左指针右移
                    l += 1
                else:   # 和>0， 右指针左移
                    r -= 1
        return result