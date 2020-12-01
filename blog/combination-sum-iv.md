Leetcode 377. 组合总和 Ⅳ
<p>给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。</p>


<p><strong>示例:</strong></p>



<pre>

<em><strong>nums</strong></em> = [1, 2, 3]

<em><strong>target</strong></em> = 4



所有可能的组合为：

(1, 1, 1, 1)

(1, 1, 2)

(1, 2, 1)

(1, 3)

(2, 1, 1)

(2, 2)

(3, 1)



请注意，顺序不同的序列被视作不同的组合。



因此输出为 <strong>7</strong>。

</pre>



<p><strong>进阶：</strong><br />

如果给定的数组中含有负数会怎么样？<br />

问题会产生什么变化？<br />

我们需要在题目中添加什么限制来允许负数的出现？</p>



<p><strong>致谢：</strong><br />

特别感谢&nbsp;<a href="https://leetcode.com/pbrother/">@pbrother</a>&nbsp;添加此问题并创建所有测试用例。</p>





 **难度**: Medium



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了99.81% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了92.02% 的用户

解题思路：
    动态规划

    以 nums = [1,2,4] target = 7为例

    target:     1       2       3       4       5       6       7
    dp:         1       2       3       6       10      18      31

        dp[i] = dp[i-1] + dp[i-2] + dp[i-4]
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in range(target+1)]
        dp[0] = 1

        for t in range(1, target+1):

            for num in nums:
                if t  < num:
                    break
                else:
                    dp[t] += dp[t-num]

        return dp[target]
</code></pre></div>
