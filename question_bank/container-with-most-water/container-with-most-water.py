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

