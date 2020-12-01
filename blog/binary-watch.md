Leetcode 401. 二进制手表
<p>二进制手表顶部有 4 个 LED 代表<strong> 小时（0-11）</strong>，底部的 6 个 LED 代表<strong> 分钟（0-59）</strong>。</p>


<p>每个 LED 代表一个 0 或 1，最低位在右侧。</p>



<p><img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg" style="height: 300px;"></p>



<p>例如，上面的二进制手表读取 &ldquo;3:25&rdquo;。</p>



<p>给定一个非负整数 <em>n&nbsp;</em>代表当前 LED 亮着的数量，返回所有可能的时间。</p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre>输入: n = 1

返回: [&quot;1:00&quot;, &quot;2:00&quot;, &quot;4:00&quot;, &quot;8:00&quot;, &quot;0:01&quot;, &quot;0:02&quot;, &quot;0:04&quot;, &quot;0:08&quot;, &quot;0:16&quot;, &quot;0:32&quot;]</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li>输出的顺序没有要求。</li>

	<li>小时不会以零开头，比如 &ldquo;01:00&rdquo;&nbsp;是不允许的，应为 &ldquo;1:00&rdquo;。</li>

	<li>分钟必须由两位数组成，可能会以零开头，比如 &ldquo;10:2&rdquo;&nbsp;是无效的，应为 &ldquo;10:02&rdquo;。</li>

	<li>超过表示范围（<strong>小时 0-11，分钟 0-59</strong>）的数据将会被舍弃，也就是说不会出现 &quot;13:00&quot;, &quot;0:61&quot; 等时间。</li>

</ul>





 **难度**: Easy



 **标签**: 位运算、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
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
</code></pre></div>
