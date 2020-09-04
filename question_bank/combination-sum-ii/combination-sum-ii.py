# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：116 ms, 在所有 Python3 提交中击败了27.35% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了69.31% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # 先进行排序，为去重做准备
        n = len(candidates)
        result = []         # 保存最终结果

        def backtrack(begin:int, current:list): # 当前数字下标，当前列表

            if sum(current) == target:          # 如果当前列表和 == 目标，加入最终结果
                result.append(current.copy())
                return
            if sum(current) > target:           # > 目标值，直接返回
                return
            for i in range(begin, n):
                if i > begin and candidates[i]== candidates[i-1]:   # 排序过了，如果当前数字已经处理过，则跳过
                    continue
                current.append(candidates[i])   # 添加到当前列表中
                backtrack(i+1, current)         # 查询下一个
                current.pop()                   # 回溯

        backtrack(0, [])
        return result


"""
执行用时：52 ms, 在所有 Python3 提交中击败了75.99% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了90.56% 的用户

解题思路：
    回溯
    基本思想与上面相同，当时不对当前列表求和，而是在每次递归时，减去当前值，生成新的目标值
    可以通过比较当前值与目标值，跳过许多不必要的循环
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []

        def backtrack(begin:int, target:int, current:list): # 当前数字下标，当前目标值，当前列表
            if target == 0:                                 # 目标值为0， 等同于当前列表和==目标值
                result.append(current.copy())
                return

            for i in range(begin, n):
                if candidates[i] > target:                  # 如果当前值大于当前目标值，则跳过之后的，因为已排序
                    return

                if i > begin and candidates[i] == candidates[i-1]:
                    continue
                current.append(candidates[i])
                backtrack(i+1, target-candidates[i], current)   # 改为更新目标值
                current.pop()

        backtrack(0,target,[])
        return result