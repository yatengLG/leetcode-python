Leetcode 18. 四数之和
<p>给定一个包含&nbsp;<em>n</em> 个整数的数组&nbsp;<code>nums</code>&nbsp;和一个目标值&nbsp;<code>target</code>，判断&nbsp;<code>nums</code>&nbsp;中是否存在四个元素 <em>a，</em><em>b，c</em>&nbsp;和 <em>d</em>&nbsp;，使得&nbsp;<em>a</em> + <em>b</em> + <em>c</em> + <em>d</em>&nbsp;的值与&nbsp;<code>target</code>&nbsp;相等？找出所有满足条件且不重复的四元组。</p>


<p><strong>注意：</strong></p>



<p>答案中不可以包含重复的四元组。</p>



<p><strong>示例：</strong></p>



<pre>给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。



满足要求的四元组集合为：

[

  [-1,  0, 0, 1],

  [-2, -1, 1, 2],

  [-2,  0, 0, 2]

]

</pre>





 **难度**: Medium



 **标签**: 数组、 哈希表、 双指针、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
行用时：1808 ms, 在所有 Python3 提交中击败了14.35% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了97.14% 的用户

解题思路：
    双指针法，总体思路同三数求和

      i  j l                                      r
    [-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5], 28
    外层i, j双循环， l, r双指针分别指向头尾。
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:       # 长度小于4，直接返回[]
            return []

        result = []
        now_i = None
        for i in range(n):
            if nums[i] == now_i:    # i去重
                continue
            now_i = nums[i]

            now_j = None
            for j in range(i + 1, n):
                if nums[j] == now_j:    # j去重
                    continue
                now_j = nums[j]

                l, r = j + 1, n - 1     # 双指针分别指向剩余字符串的头尾
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:     # 若相等
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: # 左指针去重
                            l += 1
                        while l < r and nums[r] == nums[r - 1]: # 右指针去重
                            r -= 1
                        l += 1  # 由于相等，且已排序去重。左右指针可同时向中间移动
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:    # 和小，移动左指针
                        l += 1
                    else:   # 和大，移动右指针
                        r -= 1
        return result

"""
执行用时：124 ms, 在所有 Python3 提交中击败了76.55% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了52.62% 的用户

解题思路：
    对上述代码进行优化后，速度进一步提升
    可将每次的索引值保存下来，如 num_i = nums[i]，免去每次索引应该会更快一点
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []

        result = []
        now_i = None

        for i in range(n - 3):
            if nums[i] == now_i:
                continue
            now_i = nums[i]

            if nums[i] * 4 > target:    # 当前4倍的最小值大于目标值，则后续均大于，跳出循环
                break
            if nums[i] + nums[-1] * 3 < target: # 当前最小值与3倍的最大值的和小于目标值，跳出本次循环
                continue

            now_j = None
            for j in range(i + 1, n - 2):
                if nums[j] == now_j:
                    continue
                now_j = nums[j]

                if nums[i] + nums[j] * 3 > target:  # 优化
                    break
                if nums[i] + nums[j] + nums[-1] * 2 < target:   # 优化
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return result</code></pre></div>
