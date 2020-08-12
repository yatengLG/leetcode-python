# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了84.94% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了100.00% 的用户

解题思路：
    依次计算年月日，进行天数累加，最后判断距标准日期天数

日历常识：
    当前使用公历为【格里历】，【格里历】由【儒略历】进化完善而来。
    【儒略历】变化较多，尤其前几年月份日期以及闰年等计算较乱，因而【儒略历】前期推算较为繁杂。
    【格里历】将【儒略历】1582年10月4日星期四的次日，为格里历1582年10月15日星期五，即有10天被删除。
"""
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_dict = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        week_day = 1    # 公元1912年1月1日 星期1
        month_days = [0, 31, 28 ,31, 30, 31, 30, 31, 31, 30, 31, 30]

        for y in range(1912, year):
            if ((y % 100 != 0) and (y % 4 == 0)) or (y % 400 == 0):
                week_day = week_day + 1
            week_day = (week_day + 365)

        for m in range(1, month+1):
            week_day = week_day + month_days[m-1]

        if (((year % 100 != 0) and (year % 4 == 0)) or (year % 400 == 0)) and ( month > 2):
            week_day = week_day +1

        week_day = week_day + day - 1
        return week_dict[week_day%7]
