# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：236 ms, 在所有 Python3 提交中击败了93.30% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了9.53% 的用户

解题思路：
    具体实现见代码注释
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:  # 如果长<3，False
            return False
        if not (A[0] < A[1] and A[-1] < A[-2]): # 判断起始与结尾，如不满足则直接False
            return False

        up = True   # 记录上升状态
        for i in range(1, len(A)):
            if A[i] > A[i-1] and up:    # 如果当前上升，则跳过
                pass
            elif A[i] < A[i-1]: # 如果当前下降，则将状态至于下降
                up = False
            else:   # 如果下降状态，但数值增大，或数值不变，则False
                return False
        return True