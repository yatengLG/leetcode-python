# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：152 ms, 在所有 Python3 提交中击败了96.83% 的用户
内存消耗：14 MB, 在所有 Python3 提交中击败了12.45% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0  # 5元10元初始各0个
        for bill in bills:
            if bill == 20:  # 对于20，有两种找零方式
                if five > 0 and ten > 0:    # 一张5一张10
                    five -= 1
                    ten -= 1
                elif five > 2:  # 或者 三张5
                    five -= 3
                else:           # 其余情况找不开
                    return False
            elif bill == 10 and five > 0:   # 对于10， 只能找零一张5
                five -= 1
                ten += 1
            elif bill == 5: # 5元不用找零
                five += 1
            else:
                return False
        return True