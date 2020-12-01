Leetcode 17. 电话号码的字母组合
<p>给定一个仅包含数字&nbsp;<code>2-9</code>&nbsp;的字符串，返回所有它能表示的字母组合。</p>


<p>给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。</p>



<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png" style="width: 200px;"></p>



<p><strong>示例:</strong></p>



<pre><strong>输入：</strong>&quot;23&quot;

<strong>输出：</strong>[&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].

</pre>



<p><strong>说明:</strong><br>

尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。</p>





 **难度**: Medium



 **标签**: 字符串、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：36 ms, 在所有 Python3 提交中击败了86.65% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了86.43% 的用户

解题思路：
    多重循环，依次填入字符
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            '1':[],
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }

        if digits == '':
            return []

        result = letter_dict[digits[0]]
        if len(digits) == 1:
            return result

        for s in digits[1:]:
            result_ = []
            for letter in letter_dict[s]:
                for r in result:
                    result_.append(r+letter)
            result = result_.copy()

        return result</code></pre></div>
