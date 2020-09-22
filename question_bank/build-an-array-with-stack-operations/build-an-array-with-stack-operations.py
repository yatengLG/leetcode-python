# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：28 ms, 在所有 Python3 提交中击败了99.57% 的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了38.43% 的用户

解题思路：
    用下标去查看target元素
    见代码注释
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        N = len(target)
        result = []
        for num in range(1, n+1):
            if num == target[i]:
                i += 1
                result.append('Push')   # 如果数组与元素符合，则push,且对比下一个元素
            else:
                result.append('Push')
                result.append('Pop')
                # result.extend(['Push', 'Pop'])  # 不符合，则push后pop, 用下一个数字对比
            if i > N-1:
                break
        return result

