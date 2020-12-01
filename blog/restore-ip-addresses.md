Leetcode 93. 复原IP地址
<p>给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。</p>


<p><strong>有效的 IP 地址</strong> 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>&#39;.&#39; </code>分隔。</p>



<p>例如：&quot;0.1.2.201&quot; 和 &quot;192.168.1.1&quot; 是 <strong>有效的</strong> IP 地址，但是 &quot;0.011.255.245&quot;、&quot;192.168.1.312&quot; 和 &quot;192.168@1.1&quot; 是 <strong>无效的</strong> IP 地址。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>s = &quot;25525511135&quot;

<strong>输出：</strong>[&quot;255.255.11.135&quot;,&quot;255.255.111.35&quot;]

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>s = &quot;0000&quot;

<strong>输出：</strong>[&quot;0.0.0.0&quot;]

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>s = &quot;1111&quot;

<strong>输出：</strong>[&quot;1.1.1.1&quot;]

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>s = &quot;010010&quot;

<strong>输出：</strong>[&quot;0.10.0.10&quot;,&quot;0.100.1.0&quot;]

</pre>



<p><strong>示例 5：</strong></p>



<pre><strong>输入：</strong>s = &quot;101023&quot;

<strong>输出：</strong>[&quot;1.0.10.23&quot;,&quot;1.0.102.3&quot;,&quot;10.1.0.23&quot;,&quot;10.10.2.3&quot;,&quot;101.0.2.3&quot;]

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>0 &lt;= s.length &lt;= 3000</code></li>

	<li><code>s</code> 仅由数字组成</li>

</ul>





 **难度**: Medium



 **标签**: 字符串、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
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
        return result</code></pre></div>
