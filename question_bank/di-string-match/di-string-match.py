# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：4752 ms, 在所有 Python3 提交中击败了5.05% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了16.67% 的用户

算法思想：
    两个列表，一个保存需要放入的元素， 一个用来存储结果
    如遇到I，则从列表中取出最小值，放入result中
    遇到D，则从列表中取出最大值，放入result中
"""
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        list1 = list(range(len(S) + 1))

        for s in S:
            if s == 'I':
                element = min(list1)
                result.append(element)
                list1.remove(element)
            else:
                element = max(list1)
                result.append(element)
                list1.remove(element)
        result.extend(list1)
        return result


"""
执行用时：76 ms, 在所有 Python3 提交中击败了73.40% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了16.67% 的用户
解题思路：
    由于本题中 需要存入的元素是连续的，所以直接定义俩个变量存储最大值和最小值，省去列表步骤
"""
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        min_, max_ = 0, len(S)
        for s in S:
            if s == 'I':
                result.append(min_)
                min_ += 1
            else:
                result.append(max_)
                max_ -= 1
        result.append(min_)
        return result

