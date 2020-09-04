# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了83.81% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了94.55% 的用户

解题思路：
    深度优先回溯
    对回溯算法理解不深刻，学习了官方给的解题思路
    具体实现见代码注释
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []     # 用于保存最终结果

        def backtrack(l_num, r_num, current):   # 回溯， 左括号数量，右括号数量，当前的字符串
            if l_num == 0 and r_num == 0:   # 如果左右括号均消耗完，则将当前字符串添加到结果中
                result.append(current)
                return
            if l_num > r_num:   # 如果当前剩余的左括号数量多于右括号，则存在问题
                return
            if l_num > 0:   # 如果剩余的左括号数量大于0， 则将一个左括号添加到当前字符串中，左括号数量减1
                backtrack(l_num-1, r_num, current + '(')
            if r_num > 0:   # 如果剩余的右括号数量大于0， 则将一个右括号添加到当前字符串中，右括号数量减1
                backtrack(l_num, r_num-1, current + ')')

        backtrack(n,n, "")
        return result