# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：68 ms, 在所有 Python3 提交中击败了27.10% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了34.72% 的用户

解题思路：
    循环遍历，如果相等，则调用del删除元素
    这个实际与题意不符，题中所述：返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 不需要考虑数组中超出新长度后面的元素
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1
        return len(nums)


"""
执行用时：40 ms, 在所有 Python3 提交中击败了96.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了48.50% 的用户

解题思路：
    循环，使用index记录不重复的元素个数，依次遍历列表
    重复则跳过，不重复则将当前index元素替换为不重复元素
    最终，前index个元素均不重复即可，后面元素不予考虑
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        record = None
        index = 0
        for i, value in enumerate(nums):
            if value == record:
                pass
            else:
                record = value
                nums[index] = record
                index += 1
        return index
