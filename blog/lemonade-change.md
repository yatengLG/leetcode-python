Leetcode 860. 柠檬水找零
<p>在柠檬水摊上，每一杯柠檬水的售价为&nbsp;<code>5</code>&nbsp;美元。</p>


<p>顾客排队购买你的产品，（按账单 <code>bills</code> 支付的顺序）一次购买一杯。</p>



<p>每位顾客只买一杯柠檬水，然后向你付 <code>5</code> 美元、<code>10</code> 美元或 <code>20</code> 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 <code>5</code> 美元。</p>



<p>注意，一开始你手头没有任何零钱。</p>



<p>如果你能给每位顾客正确找零，返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>[5,5,5,10,20]

<strong>输出：</strong>true

<strong>解释：

</strong>前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。

第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。

第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。

由于所有客户都得到了正确的找零，所以我们输出 true。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>[5,5,10]

<strong>输出：</strong>true

</pre>



<p><strong>示例 3：</strong></p>



<pre><strong>输入：</strong>[10,10]

<strong>输出：</strong>false

</pre>



<p><strong>示例 4：</strong></p>



<pre><strong>输入：</strong>[5,5,10,10,20]

<strong>输出：</strong>false

<strong>解释：</strong>

前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。

对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。

对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。

由于不是每位顾客都得到了正确的找零，所以答案是 false。

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ul>

	<li><code>0 &lt;= bills.length &lt;= 10000</code></li>

	<li><code>bills[i]</code>&nbsp;不是&nbsp;<code>5</code>&nbsp;就是&nbsp;<code>10</code>&nbsp;或是&nbsp;<code>20</code>&nbsp;</li>

</ul>





 **难度**: Easy



 **标签**: 贪心算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：152 ms, 在所有 Python3 提交中击败了96.83% 的用户
内存消耗：14 MB, 在所有 Python3 提交中击败了12.45% 的用户

解题思路：
    见代码注释
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0  # 5元10元初始各0个
        for bill in bills:
            if bill == 20:  # 对于20，有两种找零方式
                if five > 0 and ten > 0:    # 一张5一张10
                    five -= 1
                    ten -= 1
                elif five > 2:  # 或者 三张5
                    five -= 3
                else:           # 其余情况找不开
                    return False
            elif bill == 10 and five > 0:   # 对于10， 只能找零一张5
                five -= 1
                ten += 1
            elif bill == 5: # 5元不用找零
                five += 1
            else:
                return False
        return True
</code></pre></div>
