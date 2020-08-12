# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：52 ms
内存消耗：13.6 MB

解题思路：
    这离使用的是官方提供的 自动机 思想。
    首先，分析各字符对应的状态：
                        ' '     +-      numbel      other
            start       start   signed  innumbel    end
            signed      end     end     innumbel    end
            innumbel    end     end     innumbel    end
            end         end     end     end         end
    初始状态为 start,
    在start状态下， 若首字符为' '，则状态不变。若首字符为+-，则将状态调为 signed。 若首字符是数字，则状态调整为 innumbel， 若是其他字符，则调为 end.
    在signed状态下，若字符为数字，则将状态调整为innumbel， 否则为end
    在innumbel状态下，若字符为数字，则保持innumbel状态，否则为end

    具体实现见代码注释
"""
class Solution:
    def myAtoi(self, str: str) -> int:
        am = AM()
        for c in str:
            if am.state == 'end':
                break
            am.get(c)
        return am.sign * am.num


class AM:
    def __init__(self):
        self.tabel = {
            'start': ['start', 'signed', 'innumbel', 'end'],
            'signed': ['end', 'end', 'innumbel', 'end'],
            'innumbel': ['end', 'end', 'innumbel', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }                       # 状态表
        self.sign = 1           # 初始符号为正
        self.num = 0            # 用于存储转换后的数字
        self.state = 'start'    # 初始状态为start
        self.max_ = 2**31 - 1   # 最大数值限制，这里初始限制为 2**31-1 （正数）

    def get_col(self, c:str) -> int:    # 首字符判断，返回为状态表列的索引
        if c.isdigit():
            return 2    # innumbel
        if c.isspace():
            return 0    # start
        if c == '+' or c == '-':
            return 1    # signed
        else:
            return 3    # end

    def get(self, c):
        self.state = self.tabel[self.state][self.get_col(c)]
        if self.state == 'start':   # start 不操作，继续下一个字符
            pass
        if self.state == 'signed':  # signed 将状态调整为signed，且对初始符号与最大数值进行调整
            if c == '+':
                self.sign = 1
            else:
                self.sign = -1
                self.max_ = self.max_ + 1   # 负数时，2**31

        if self.state == 'innumbel':    # innumbel 状态时，计算数值且累加
            self.num = self.num *10 + int(c)
            if self.num > self.max_:    # 若超出数值限制，则将状态置为end
                self.num = self.max_
                self.state = 'end'

        if self.state == 'end':     # end 不做操作
            pass

