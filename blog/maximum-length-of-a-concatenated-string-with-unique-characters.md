Leetcode 1239. 串联字符串的最大长度
<p>给定一个字符串数组 <code>arr</code>，字符串 <code>s</code> 是将 <code>arr</code> 某一子序列字符串连接所得的字符串，如果 <code>s</code> 中的每一个字符都只出现过一次，那么它就是一个可行解。</p>


<p>请返回所有可行解 <code>s</code> 中最长长度。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>arr = [&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;]

<strong>输出：</strong>4

<strong>解释：</strong>所有可能的串联组合是 &quot;&quot;,&quot;un&quot;,&quot;iq&quot;,&quot;ue&quot;,&quot;uniq&quot; 和 &quot;ique&quot;，最大长度为 4。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>arr = [&quot;cha&quot;,&quot;r&quot;,&quot;act&quot;,&quot;ers&quot;]

<strong>输出：</strong>6

<strong>解释：</strong>可能的解答有 &quot;chaers&quot; 和 &quot;acters&quot;。

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>arr = [&quot;abcdefghijklmnopqrstuvwxyz&quot;]

<strong>输出：</strong>26

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>1 &lt;= arr.length &lt;= 16</code></li>

	<li><code>1 &lt;= arr[i].length &lt;= 26</code></li>

	<li><code>arr[i]</code>&nbsp;中只含有小写英文字母</li>

</ul>





 **难度**: Medium



 **标签**: 位运算、 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：156 ms, 在所有 Python3 提交中击败了34.91% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了7.28% 的用户

解题思路：
    回溯
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = []    # 用于存放所有结果
        n = len(arr)

        def backtrack(begin, current:str):  # 起始位置，当前合并字符串
            results.append(current) # 把当前结果存入最终结果中
            if begin == n:  # 如果遍历结束，则结束
                return
            for i in range(begin, n):   # 从起始位置一直向后遍历
                if len(set(current+arr[i])) != len(current+arr[i]): # 如果当前字符串存在重复元素，则跳出，继续下一个
                    continue
                backtrack(i, current+arr[i])    # 处理下一个字符串
                # 因为是字符串，且，传入的是current+arr[i], 这里不需要进行额外处理
        backtrack(0, '')
        result = 0
        for r in results:
            if len(r) > result:
                result = len(r)
        return result


"""
执行用时：156 ms, 在所有 Python3 提交中击败了34.91% 的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了96.12% 的用户

代码经过精简后
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.result = 0
        n = len(arr)

        def backtrack(begin, current:str):

            if len(current) > self.result:
                self.result = len(current)

            for i in range(begin, n):
                if len(set(current+arr[i])) != len(current+arr[i]):
                    continue
                backtrack(i, current+arr[i])

        backtrack(0, '')

        return self.result
</code></pre></div>
