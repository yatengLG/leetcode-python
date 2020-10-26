# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了97.12% 的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了78.97% 的用户

解题思路：
    模拟提议，记录当前起伏状态，分析是否是山脉
    具体实现见代码注释
"""
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        s, p, l = 0, 0, 0   # 起始点，p指针，记录当前最长山脉长度
        up, down = False, False # 记录当前起伏状态
        while p < len(A)-1:
            if A[p] > A[p+1]: # 当前下降
                if up:  # 如果之前存在上升状态，则存在山脉，激活山脉的下降状态
                    down = True
                else:
                    s = p+1 # 否则，之前不存在山脉，将挪动起始点
            elif A[p] < A[p+1]:   # 当前上升
                if up == True and down == True: # 如果上升和下降状态激活， 则存在山脉，且山脉结束
                    l = max(l, p+1-s)   # 更新山脉长度
                    s = p   # 挪动起始点
                    down = False    # 重置起伏状态
                up = True
            else:   # 平地
                if up == True and down == True: # 如果之前存在山脉，则更新l
                    l = max(l, p+1 - s)
                up = False  # 重置起伏状态
                down = False
                s = p+1 # 挪动起始点
            p += 1
        if up == True and down == True: # 如果存在山脉，则更新l
            l = max(l, p+1 - s )
        return l