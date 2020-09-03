# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了48.88% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了94.96% 的用户

解题思路：
    回溯, 参考https://leetcode-cn.com/problems/binary-watch/solution/hui-su-jian-zhi-qu-zhong-by-boille/
    将代表时分的灯排列到一起
        0   1   2   3   4   5   6   7   8   9
        0   2   4   8   0   2   4   8   16  32
        h   h   h   h   m   m   m   m   m   m

    前四个为代表小时的灯， 后六个为代表分钟的灯

    具体实现见代码注释
"""
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []         # 最终结果
        hour_seen = set()   # 用于记录用过的小时的灯 的序号
        minute_seen = set() # 用于记录用过的分钟的灯 的序号

        def backstrace(num:int, hour:int, minute:int, which:int) -> None:
            """

            :param num:     灯的数量
            :param hour:    当前小时
            :param minute:  当前分钟
            :param which:   当前开始遍历的灯的序号， 去重使用。
            :return:
            """
            if hour > 11 or minute > 59:    # 终止条件。小时大于11， 分钟大于59
                return

            if num == 0:    # 等于0时，则所以灯都用过了，添加到最终结果中
                result.append("{}:{:0>2d}".format(hour, minute))

            for h in range(which, 4):   # 小时灯序号 0~3
                if h not in hour_seen:  # 当前灯序号未使用过
                    hour_seen.add(h)    # 记录
                    backstrace(num-1, hour+ int(pow(2, h)),minute, h+1) # 在小时灯范围 使用下一个亮着的灯， num-1, hour增加
                    hour_seen.remove(h)

            for m in range(max(which, 4), 10):  # 分钟灯，范围4~9
                if m not in minute_seen:
                    minute_seen.add(m)
                    backstrace(num-1, hour, minute + int(pow(2, m-4)), m+1)
                    minute_seen.remove(m)

        backstrace(num, 0, 0, 0)

        return result