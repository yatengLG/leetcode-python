# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了83.86% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了62.52%

解题思路：
    对拼消耗，摩尔投票
    时间复杂度为 O(N)，空间复杂度为 O(1)
    不同数字一一对拼消耗，如果有剩余，则存在主要元素(人数最多，且，人数在一半以上)
    具体实现见代码注释
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = nums[0] # 记录当前元素
        count = 0   # 当前元素的出现次数统计
        for i in range(n):
            if nums[i] == major:    # 如果与当前元素相同，则次数+1
                count += 1
            else:   # 不同，则对拼消耗，次数减一
                count -= 1
            if count == 0 and i < n-1:  # 如果当前元素被消耗殆尽，当前元素指向下一个元素
                major = nums[i+1]

        if count > 0:   # 如果当前元素的统计次数大于0，则存在主要元素
            return major
        else:       # 否则，不存在
            return -1