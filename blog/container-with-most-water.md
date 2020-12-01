Leetcode 11. 盛最多水的容器
<p>给你 <em>n</em> 个非负整数 <em>a</em><sub>1</sub>，<em>a</em><sub>2，</sub>...，<em>a</em><sub>n，</sub>每个数代表坐标中的一个点&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 。在坐标内画 <em>n</em> 条垂直线，垂直线 <em>i</em>&nbsp;的两个端点分别为&nbsp;(<em>i</em>,&nbsp;<em>a<sub>i</sub></em>) 和 (<em>i</em>, 0)。找出其中的两条线，使得它们与&nbsp;<em>x</em>&nbsp;轴共同构成的容器可以容纳最多的水。</p>


<p><strong>说明：</strong>你不能倾斜容器，且&nbsp;<em>n</em>&nbsp;的值至少为 2。</p>



<p>&nbsp;</p>



<p><img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" style="height: 287px; width: 600px;"></p>



<p><small>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</small></p>



<p>&nbsp;</p>



<p><strong>示例：</strong></p>



<pre><strong>输入：</strong>[1,8,6,2,5,4,8,3,7]

<strong>输出：</strong>49</pre>





 **难度**: Medium



 **标签**: 数组、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了85.40% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了41.13% 的用户

解题思路：
    双指针法

                                |
                        |       |           |
                        |       |           |       |
                        |       |           |       |
                    ---------------------------------------

    高度方面：水面的高度，取决于两侧最低的一侧。也就是说，只要确定最低的一侧，中间区域的水位高度就不会高于当前高度
    宽度方面：由于我们是从俩侧依次往中间挪动，水面的宽度也不会大于我们的当前宽度。
    最终结论：当前的两堵墙间的最大面积，已经被矮墙限制，无需考虑。
        我们只需移动矮墙，去在剩下的较高墙体之间寻找最大面积即可

    具体实现见代码注释.
"""
class Solution:
    def maxArea(self, height) -> int:
        p, q = 0, len(height)-1     # p, q 双指针，分别指向头、尾
        max_ = 0
        while q-p > 0:      # 若双指针已遍历完，则退出循环
            h_p, h_q = height[p], height[q] # 双指针指向的墙体高度
            if h_p < h_q:       # 向中间移动矮墙指针，记录并更新最大面积
                area = h_p * (q - p)
                if area > max_:
                    max_ = area
                p += 1
            else:
                area = h_q * (q - p)
                if area > max_:
                    max_ = area
                q -= 1
        return max_


"""
暴力破解，在leetcode上是行不通的，超时了
"""
class Solution:
    def maxArea(self, height) -> int:
        nums = len(height)
        max_ = 0
        for i in range(nums):
            for j in range(i+1, nums):
                area = (j-i) * min(height[i], height[j])
                if area> max_:
                    max_ = area
        return max_

</code></pre></div>
