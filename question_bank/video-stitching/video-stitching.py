# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了98.92% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了32.75% 的用户

解题思路：
    动态规划
    具体实现见代码注释
"""
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        dp = [float('inf')] * (T+1) # 剪切到当前位置所需的最小次数
        dp[0] = 0
        for clip in clips:
            start, end = clip[0], clip[1]   # 每个片段起始与结尾
            for i in range(start, end+1):
                if i > T:   # 当前片段结尾可能超出所需长度
                    break
                dp[i] = min(dp[start]+1, dp[i]) # 当前片段，最小次数为起始处的次数+1
        if dp[-1] == float('inf'):
            return -1
        else:
            return int(dp[-1])