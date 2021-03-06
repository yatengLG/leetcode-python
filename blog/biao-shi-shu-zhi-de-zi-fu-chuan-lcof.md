Leetcode 剑指 Offer 20. 表示数值的字符串
<p>请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串&quot;+100&quot;、&quot;5e2&quot;、&quot;-123&quot;、&quot;3.1416&quot;、&quot;-1E-16&quot;、&quot;0123&quot;都表示数值，但&quot;12e&quot;、&quot;1a3.14&quot;、&quot;1.2.3&quot;、&quot;+-5&quot;及&quot;12e+5.4&quot;都不是。</p>


<p>&nbsp;</p>





 **难度**: Medium



 **标签**: 数学、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：48 ms, 在所有 Python3 提交中击败了55.80% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了16.54% 的用户

解题思路：
    有限状态自动机

    字符可分为：
        1. ""             空格
        2. '0123456789'   数字
        3. '+-'           正负号
        4. '.'            小数点
        5. 'e,E'          指数符号
    状态可分为：
        1. 起始状态
            起始状态需要考虑 空格问题。 且不能直接e开头
        2. e前正负号
            e前后均可存在正负数。
        3. .前数字
            .前数字为整数，其后可以接小数点构成小数
        4. .后数字
            .后数字已经是小数，不可接小数点
        5. ''.后数字       例： .6   .13
            .5 是合法的， 但这种形式不以接e。  例： .5e4 是不合法的, 合法写法应是5e3
        6. e
            e后可以接数字，或接正负号
        7. e后符号
            e后符号，只能接数字
        8. e后数字
            e后数字只能接数字
        9. 空格
            处理结尾空格
    具体实现见代码注释
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {'空格': 0,       '数字': 2,        '正负号': 1,       '小数点': 4,       'e': None}, # 起始。       忽略起始空格，可由数字、正负号、小数点开头
            {'空格': None,    '数字': 2,        '正负号': None,    '小数点': 4,       'e': None}, # e前正负号。   正负号后可接数字或正负号
            {'空格': 8,       '数字': 2,        '正负号': None,    '小数点': 3,       'e': 5},    # .前数字。     .前数字即为整数，可接小数点、数字、e
            {'空格': 8,       '数字': 3,        '正负号': None,    '小数点': None,    'e': 5},    # .后数字。     小数点后数字可接e、数字。 例： 1.23e10合法
            {'空格': None,    '数字': 3,        '正负号': None,    '小数点': None,    'e': None}, # ''.后数字。   例： .4 合法， 但后不能接e, .4e3不合法，合法写法应是4e2。
            {'空格': None,    '数字': 7,        '正负号': 6,       '小数点': None,    'e': None}, # e。          e后可接数字或 正负号。
            {'空格': None,    '数字': 7,        '正负号': None,    '小数点': None,    'e': None}, # e后正负号。   e后正负号后只可接数字
            {'空格': 8,       '数字': 7,        '正负号': None,    '小数点': None,    'e': None}, # e后数字。     e后数字只可接数字
            {'空格': 8,       '数字': None,     '正负号': None,    '小数点': None,    'e': None}, # 末尾空格。
        ]
        state = states[0]
        for c in s:
            if c == ' ':
                c = '空格'
            elif c in '0123456789':
                c = '数字'
            elif c in '+-':
                c = '正负号'
            elif c == '.':
                c = '小数点'
            elif c in 'eE':
                c = 'e'
            else:
                return False

            id = state[c]
            if id == None:
                return False

            state = states[state[c]]
        return state['空格'] in [2,3,7,8]
</code></pre></div>
