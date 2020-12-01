Leetcode 127. 单词接龙
<p>给定两个单词（<em>beginWord&nbsp;</em>和 <em>endWord</em>）和一个字典，找到从&nbsp;<em>beginWord</em> 到&nbsp;<em>endWord</em> 的最短转换序列的长度。转换需遵循如下规则：</p>


<ol>

	<li>每次转换只能改变一个字母。</li>

	<li>转换过程中的中间单词必须是字典中的单词。</li>

</ol>



<p><strong>说明:</strong></p>



<ul>

	<li>如果不存在这样的转换序列，返回 0。</li>

	<li>所有单词具有相同的长度。</li>

	<li>所有单词只由小写字母组成。</li>

	<li>字典中不存在重复的单词。</li>

	<li>你可以假设 <em>beginWord</em> 和 <em>endWord </em>是非空的，且二者不相同。</li>

</ul>



<p><strong>示例&nbsp;1:</strong></p>



<pre><strong>输入:</strong>

beginWord = &quot;hit&quot;,

endWord = &quot;cog&quot;,

wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]



<strong>输出: </strong>5



<strong>解释: </strong>一个最短转换序列是 &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,

     返回它的长度 5。

</pre>



<p><strong>示例 2:</strong></p>



<pre><strong>输入:</strong>

beginWord = &quot;hit&quot;

endWord = &quot;cog&quot;

wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]



<strong>输出:</strong>&nbsp;0



<strong>解释:</strong>&nbsp;<em>endWord</em> &quot;cog&quot; 不在字典中，所以无法进行转换。</pre>





 **难度**: Medium



 **标签**: 广度优先搜索、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：100 ms, 在所有 Python3 提交中击败了98.78% 的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了81.88% 的用户

解题思路:
    具体实现见代码注释
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList or len(beginWord) != len(endWord):
            return 0

        wordSet, record = set(wordList), set()
        head, tail = {beginWord}, {endWord} # 头，尾集合
        result = 1
        while head:
            wordSet -= record   # 总的wordlist 减去 record未匹配成的。
            record = set()      # 用于记录未匹配的
            if len(head) > len(tail):
                head, tail = tail, head # 为了减少循环次数，每次从最短的集合开始。 也就是每次从当前wordset中 匹配头尾集合中最短的那个

            for word in head:
                for i in range(len(beginWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        now = word[:i]+c+word[i+1:] # 转换一个字符后的单词

                        if now in tail: # 如果当前单词在另一个集合中，则可以转换成功，返回当前转换次数即可
                            return result+1
                        if now in wordSet:  # 如果当前单词在wordset中，即当前单词存在但不能匹配，添加到未匹配成功集合中
                            record.add(now)
            head = record   #
            result += 1
        return 0
</code></pre></div>
