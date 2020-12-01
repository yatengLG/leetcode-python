Leetcode 面试题 05.06. 整数转换
<p>整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。</p>


<p> <strong>示例1:</strong></p>



<pre>

<strong> 输入</strong>：A = 29 （或者0b11101）, B = 15（或者0b01111）

<strong> 输出</strong>：2

</pre>



<p> <strong>示例2:</strong></p>



<pre>

<strong> 输入</strong>：A = 1，B = 2

<strong> 输出</strong>：2

</pre>



<p> <strong>提示:</strong></p>



<ol>

<li>A，B范围在[-2147483648, 2147483647]之间</li>

</ol>





 **难度**: Easy



 **标签**: 位运算、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：44 ms, 在所有 Python3 提交中击败了35.20% 的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了100.00% 的用户
解题思路：
    这里出现了个坑，之前一直没注意
    原先直接写的  return bin(A ^ B).replace('0b','').count('1')
    & 按位与

    但一直出错，后面看解题发现：
    ```
        一般来讲，整形数在内存中是以 补码 的形式存放的，输出的时候同样也是按照 补码 输出的。
        但是在python中：
            1. 整形是以 补码 形式存放的，输出的时候是按照 二进制 表示输出的；
            2. 对于 bin(x)bin(x)bin(x)（xxx 为 十进制负数），输出的是它的原码的二进制表示加上一个负号，方便查看（方便个🔨🔨🔨）
            3. 对于 bin(x)bin(x)bin(x)（xxx 为 十六进制负数），输出的是对应的二进制表示。
        所以为了获得十进制负数的补码，我们需要手动将其和 0xffffffff 进行与操作，得到一个十六进制数，再交给 bin() 转化，这时内存中得到的才是你想要的补码。

        作者：z1m
        链接：https://leetcode-cn.com/problems/convert-integer-lcci/solution/yi-huo-jie-fa-python-3-c-by-z1m/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    ```

"""
class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A & 0xffffffff) ^ (B & 0xffffffff)).replace('0b','').count('1')
</code></pre></div>
