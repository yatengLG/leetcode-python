# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：1164 ms, 在所有 Python3 提交中击败了29.38% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了60.35% 的用户

解题思路：
    分析情况：
        1. p 为'', 则，True if s=='' else False
        2. s 为空 False
        3. 首字符是否匹配， 若p[0]==s[0] or p[0]=='.'
            首字符匹配的情况下：
                如果p长度大于1：
                    若 p[1] == '*'
                        这里需要判断两种情况： 这俩种情况，只要有一个满足即可返回true
                            s = aaa, p = a*a    p 还从第1个字符匹配。s从第2个字符匹配
                            s = a, p=a*a        p 还从第3个字符匹配。s从第1个字符匹配
                    若 p[1] != '*', 则 p、s均从第2个字符开始匹配。
                如果长度不大于1：
                    首字母是否匹配

            首字符不匹配的情况下：
                若 p[1] == '*', 则 p 从第3个字符匹配。s从第2个字符匹配

"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if s:
            first_c = (p[0]==s[0]) or (p[0]=='.')

            if first_c:
                if len(p)>1 and p[1] == '*':
                    return self.isMatch(s[1:], p) or  self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s[1:], p[1:])
            else:
                if len(p)>1 and p[1] == '*':
                    return self.isMatch(s, p[2:])
                else:
                    return False
        else:
            if len(p)>1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            return False

"""
执行用时：68 ms, 在所有 Python3 提交中击败了64.13% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了53.28%

解题思想：
    动态规划
    字符串匹配， s[：i] 与 p[:j] 是否匹配，需要看 s[i]与p[j]是否 匹配， 以及 s[:i-1]与p[:j-1] 的匹配情况
    
    若 p[j] == s[i] or p[j] == '.', 则 s[i] 与p[j] 匹配，看 s[:i-1]与p[:j-1]的匹配情况
    若 p[j] == '*':
        p[j-1] == s[i] or p[j-1] == '.' 时，*号前面字符匹配，此时有两种情况：
            *号前面字符匹配0次，此时 需看 s[:i]与p[:j-2]的匹配情况     c ca* 匹配， c va*  不匹配
            *号前面字符匹配多次,此时 需看 s[:i-1] 与 p[:j]的匹配情况   aa a*
        p[j-1] != s[i], 也就是*号前面字符匹配了0次，此时 需看 p[:j-2] 与 s[:i] 的匹配情况
    其他情况均不匹配。

    i/j     0           1           2           3        4
    0                   i-1,j-1     i-1,j
    1       i,j-2                   i,j
    2       
    
    由于p不会由*开头，为了统一处理逻辑，在表格左上侧多添加一列
    
    具体实现见代码注释
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:           # p == '' and s == '' return True
            return not s    # p == '' and s ！= '' return False

        if len(p) < 2 and not s:    # len(p) == 1 and s == '' return False
            return False

        len_s, len_p = len(s), len(p)

        # 动态规划矩阵
        dp = [[False for _ in range(len_p+1)] for _ in range(len_s+1)]

        # 0,0 对应 ''  '' 所以为True
        dp[0][0] = True
        for j in range(1, len_p):   # '' 对应的 a*   a*b* 等为True
            if p[j] == '*':
                dp[0][j +1] = dp[0][j-2 +1]

        # 开始填表，这里需要注意的是，因为表中多添加了一行一列, 这里i,j索引 还是从0开始的，所以在查表以及填表时，均做了+1 操作
        for i in range(len_s):
            for j in range(len_p):
                if s[i] == p[j] or p[j] == '.': # 字符匹配时，看之前字符是否匹配即可
                    dp[i +1][j +1] = dp[i-1 +1][j-1 +1] # 查表 以及 填表，这么写是为了好理解 dp[i-1 +1][j-1 +1] 对应字符串索引(i-1,j-1)，对应表中位置为(i-1+1,j-1+1)
                if p[j] == '*': # 如匹配项为*，分俩种情况
                    if p[j-1] == s[i] or p[j-1]=='.':   # 前一项字符相配时，存在匹配0次 或多次情况
                        dp[i +1][j +1] = dp[i +1][j-2 +1] or dp[i-1 +1][j +1]   # dp[i-1 +1][j +1] 匹配多次情况； dp[i +1][j-2 +1] 匹配0次情况
                    else:
                        dp[i +1][j +1] = dp[i +1][j-2 +1]   # 前一项字符匹配，默认*匹配0次
        return dp[len_s][len_p]

"""
其实，匹配项为*时，不需要判断前一项是否匹配，只需确认匹配0次及多次即可。
"""