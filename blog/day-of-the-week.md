Leetcode 1185. 一周中的第几天
<p>给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。</p>


<p>输入为三个整数：<code>day</code>、<code>month</code> 和&nbsp;<code>year</code>，分别表示日、月、年。</p>



<p>您返回的结果必须是这几个值中的一个&nbsp;<code>{&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}</code>。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>day = 31, month = 8, year = 2019

<strong>输出：</strong>&quot;Saturday&quot;

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>day = 18, month = 7, year = 1999

<strong>输出：</strong>&quot;Sunday&quot;

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>day = 15, month = 8, year = 1993

<strong>输出：</strong>&quot;Sunday&quot;

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>给出的日期一定是在&nbsp;<code>1971</code> 到&nbsp;<code>2100</code>&nbsp;年之间的有效日期。</li>

</ul>





 **难度**: Easy



 **标签**: 数组、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
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
</code></pre></div>
