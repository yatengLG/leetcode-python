# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：104 ms, 在所有 Python3 提交中击败了95.17% 的用户
内存消耗：36.3 MB, 在所有 Python3 提交中击败了6.94% 的用户

解题思路：
    厄拉多塞筛法
    https://leetcode-cn.com/problems/count-primes/solution/pythonzui-you-jie-fa-mei-you-zhi-yi-liao-ba-by-bru/
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:   # 1, 2 不存在质数
            return 0
        record = [1] * n    # 记录质数，record[i]=1 表示， i+1是质数
        record[0], record[1] = 0, 0  # 1, 2不是质数
        for i in range(2, int(n**0.5)+1):
            if record[i]:
                record[i*i:n:i] = [0]*((n-1-i*i)//i+1)  # 如果当前i是质数，则2*i， 3*i ... 均不是质数
        return sum(record)

