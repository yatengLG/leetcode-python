Leetcode 649. Dota2 参议院
<p>Dota2 的世界里有两个阵营：<code>Radiant</code>(天辉)和 <code>Dire</code>(夜魇)</p>


<p>Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的<code><strong>一</strong></code>项：</p>



<ol>

	<li>

	<p><code>禁止一名参议员的权利</code>：</p>



	<p>参议员可以让另一位参议员在这一轮和随后的几轮中丧失<strong>所有的权利</strong>。</p>

	</li>

	<li>

	<p><code>宣布胜利</code>：</p>

	</li>

</ol>



<p>          如果参议员发现有权利投票的参议员都是<strong>同一个阵营的</strong>，他可以宣布胜利并决定在游戏中的有关变化。</p>



<p> </p>



<p>给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 <code>Radiant</code>（天辉）和 <code>Dire</code>（夜魇）。然后，如果有 <code>n</code> 个参议员，给定字符串的大小将是 <code>n</code>。</p>



<p>以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。</p>



<p>假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 <code>Radiant</code> 或 <code>Dire</code>。</p>



<p> </p>



<p><strong>示例 1：</strong></p>



<pre>

<strong>输入：</strong>"RD"

<strong>输出：</strong>"Radiant"

<strong>解释：</strong><code>第一个参议员来自 Radiant 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人</code>

</pre>



<p><strong>示例 2：</strong></p>



<pre>

<strong>输入：</strong>"RDD"

<strong>输出：</strong>"Dire"

<strong>解释：</strong>

第一轮中,第一个<code>来自 Radiant 阵营的</code>参议员可以使用第一项权利禁止第二个参议员的权利

第二个<code>来自 Dire 阵营的</code>参议员会被跳过因为他的权利被禁止

第三个<code>来自 Dire 阵营的</code>参议员可以使用他的第一项权利禁止第一个参议员的权利

因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利

</pre>



<p> </p>



<p><strong>提示：</strong></p>



<ul>

	<li>给定字符串的长度在 <code>[1, 10,000]</code> 之间.</li>

</ul>



<p> </p>





 **难度**: Medium



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：96 ms, 在所有 Python3 提交中击败了56.10% 的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了25.77% 的用户

解题思路：
    模拟
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)   # 将字符串转换为列表，便于操作
        start = senate[0]   # 当前哪个阵营行使权利
        start_n = 0 # 统计当前行使权利的行使权数
        while len(set(senate)) != 1:    # 当议院只剩一个阵营时跳出
            i = 0   # 列表索引
            while i < len(senate):
                if senate[i] == start:  # 如果当前议员属于行使权利的阵营，则当前阵营行使权+1，处理下一个议员
                    start_n += 1
                    i += 1
                else:   # 如果当前议员属于行使权利阵营的对立阵营，则行使权利的阵营禁止该议员，行使权利的阵营行使权-1
                    del senate[i]   # 删除该议员
                    start_n -= 1    # 行使权-1
                    if start_n < 1: # 若行使权==0，则 行使权利的阵营转变
                        start = senate[i] if i < len(senate) else senate[0]
                        start_n = 0
        return 'Radiant' if senate[0]=='R' else 'Dire'

</code></pre></div>
