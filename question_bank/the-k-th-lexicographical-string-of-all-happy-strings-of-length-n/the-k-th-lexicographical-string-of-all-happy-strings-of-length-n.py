# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：224 ms, 在所有 Python3 提交中击败了19.92% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了27.04% 的用户

解题思路：
    回溯
    找出所有的结果
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letter = ['a', 'b', 'c']
        result = []

        def backtrack(current):
            if len(current) >= n:   # 长度限定，如果长度达到n,则添加到最终结果，并终止
                result.append(''.join(current))
                return

            for i in range(3):
                if current == [] or (letter[i] != current[-1]): # 当前列表为[] 或 当前字母与当前列表最后一个不同时， 添加到当前列表
                    current.append(letter[i])
                    backtrack(current)
                    current.pop()   # 回溯

        backtrack([])
        if k > len(result):
            return ''
        else:
            return result[k-1]

"""
执行用时：40 ms, 在所有 Python3 提交中击败了94.74% 的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了93.71% 的用户

解题思路：
    分析状态，找规律
    
    1   a       b       c
    2   ab      ac      ba      bc      ca      cb
    3   aba     abc     aca     acb     bab     bac     bca     bcb     cab     cac     cba     cbc
    4   abab    abac    abca    abcb    acab    acac    acba    acbc    baba    babc    baca    bacb    ...

                  all               a开头     b开头     c开头
    1       3*2**(1-1) = 3*1        1           1       1    
    2       3*2**(2-1) = 3*2        2           2       2
    3       3*2**(3-1) = 3*4        4           4       4
    4       3*2**(4-1) = 3*8        8           8       8
    10      3*2**(10-1)= 3*512      512         512     512    
    需注意的是，当以b开头时，第一个字符是a，第二个是c,需将上一位存在的元素剔除
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        all_num = 3 * 2 ** (n - 1)
        if k > all_num:
            return ''
        result = []

        def find(i, k, pre):    # 当前为位数，当前找第几个数，前一个字符
            letters = ['a', 'b', 'c']
            if pre in letters:
                letters.remove(pre) # 从a,b,c 中移除，上一个字符。确保相邻元素不同
            index = k // 2 ** (n - 1 - i)   # 整除获得下标，依据下标取当前位的字符
            k = k % 2 ** (n - 1 - i)        # 余数，作为新的k
            result.append(letters[index])
            return k, letters[index]

        pre = ''
        k = k - 1
        for i in range(n):
            k, pre = find(i, k, pre)
        return ''.join(result)
