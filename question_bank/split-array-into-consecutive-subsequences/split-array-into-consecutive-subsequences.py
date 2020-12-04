# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了90.08% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了43.72% 的用户

"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)    # 统计nums中每个数的出现次数
        endMap = collections.Counter()  # 统计以num结尾的子序列的个数

        for num in nums:
            if countMap[num]:
                if endMap.get(num-1):   # 如果存在子序列以 num-1 结尾，则，把当前数 添加到该序列后
                    countMap[num] -= 1  # 当前数统计次数-1
                    endMap[num-1] -= 1  # 以num-1为结尾的子序列-1
                    endMap[num] += 1    # 以num为结尾的子序列+1
                else:
                    if countMap.get(num+1) and countMap.get(num+2): # 如果num, num+1, num+2 均存在，则此三个数构成一个新的子序列
                        endMap[num+2] += 1      # 以num+2为结尾的子序列+1
                        countMap[num] -= 1      # num统计次数-1
                        countMap[num+1] -= 1    # num+1统计次数-1
                        countMap[num+2] -= 1    # num+2统计次数-1
                    else:
                        return False
        return True
