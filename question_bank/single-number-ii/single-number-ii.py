# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了74.80% 的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了49.88% 的用户

解题思路：
    位运算
        异或 ^
            x ^ 1 = ~x
            x ^ 0 = x
        与运算 &
            x & 1 = x
            x & 0 = 0

    计算[10,10,3,10]
        1010
        1010
        0011
        1010
    =   0011
    每位对3取余

    余数存在三种情况 0, 1, 2，使用one,two来表示三种情况
        情况  two one
        0       0   0
        1       0   1
        2       1   0

    三种情况的转换 0 -> 1 -> 2 -> 0 -> 1 -> ……
        使用one，two表示的的状态的转换 00 -> 01 -> 10 -> 00 -> ……
        先固定 two 更新 one
            two -> one:
                if two == 0:
                    if x == 0:
                        one = one
                    if x == 1:
                        one = ~one
                if two == 1:
                    one = 0
            使用位运算简化上述过程:
                if two == 0:
                    one = one ^ x
                if two == 1:
                    one = 0
            进一步简化:
                one = one ^ x & ~two

        更新完one,状态由 00 -> 01 -> 10 变为 01 -> 00 -> 10
            情况  two one
                    0   1
                    0   0
                    1   0
            固定one， 更新two
                if one == 0:
                    if x == 0:
                        two = two
                    if x == 1:
                        two = ~ two
                if two == 1:
                    one = 0
            同理：
                two = two ^ x & ~one



"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one = one ^ num & ~two
            two = two ^ num & ~one
        return one