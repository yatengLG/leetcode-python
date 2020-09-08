# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：40 ms, 在所有 Python3 提交中击败了89.64% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了68.81% 的用户

解题思路：
    回溯
    具体实现见代码注释
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(s, current:list): #   当前字符串，当前ip列表
            # print(s, current)
            if s =='' and len(current) == 4:    # 如果字符串全使用，且当前ip长度刚好4位。则完全匹配
                result.append(current[:])       # 添加到最终结果中
                return

            if ((4-len(current)) * 3 < len(s)): # 如果 剩余字符串数量，大于当前缺失的ip*3 则，字符串冗余，跳出
                return

            for i in range(min(3, len(s))):     # ip每一位最大3个字符
                if (s[0] == '0' and i < 1) or (s[0] != '0' and 0< (int(s[:i+1]) < 256)):    # 当前字符，以0开头使，只能匹配0； 或不以0开头且在0～255之间
                    current.append(s[:i+1])
                    now_s = s[i+1:]
                    backtrack(now_s, current)   # 从剩余字符串中匹配下一位
                    current.pop()   # 回溯

        backtrack(s, [])
        result = [ '.'.join(i) for i in result] # 格式化字符串
        return result