Leetcode 面试题 08.01. 三步问题
<p>三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。</p>


<p> <strong>示例1:</strong></p>



<pre>

<strong> 输入</strong>：n = 3 

<strong> 输出</strong>：4

<strong> 说明</strong>: 有四种走法

</pre>



<p> <strong>示例2:</strong></p>



<pre>

<strong> 输入</strong>：n = 5

<strong> 输出</strong>：13

</pre>



<p> <strong>提示:</strong></p>



<ol>

<li>n范围在[1, 1000000]之间</li>

</ol>





 **难度**: Easy



 **标签**: 动态规划、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
超时
解题思路：
    动态规划，当n非常大时，需要循环计算n次，超时
"""
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        dp = [[] for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4

        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]%1000000007

"""
执行用时：2020 ms, 在所有 Python3 提交中击败了5.18% 的用户
内存消耗：29.1 MB, 在所有 Python3 提交中击败了51.83% 的用户


解题思路：
    优化，快速幂
                                  [[1,1,0],
    [ dp[i-1], dp[i-2], dp[i-3]]*  [1,0,1],  = dp[i-1]+dp[i-2]+dp[i-3], dp[i-1], dp[i-2]
                                   [1,0,0]]
    
    通过上式，可以快速得出，dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
    可得出：
                                              [[1,1,0],
        [dp[i], dp[i-1], dp[i-2]] = [1,2,4] *  [1,0,1], ^^n-3
                                              [1,0,0]]
    也就是，[1,2,4] * A ** (n-3)
    为快速计算A**n,使用快速幂方法计算
    
    快速幂：
        计算a**n 次方时，
         若n为偶数，可先计算 a**(n/2) ，然后计算 (a**(n/2))**2
         若n为奇数，可先计算 a**((n-1)/2), 然后计算 a*a**((n-1)/2)**2  
         
"""
import numpy as np

class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        if n == 4:
            return 7
        init_array = np.array([4, 2, 1], dtype=np.int64)
        A = np.array([[1, 1, 0], [1, 0, 1], [1, 0, 0]], dtype=np.int64)
        A1 = A.astype(np.int64)
        if (n - 3) % 2 == 0:
            for i in range(int((n - 3) / 2 - 1)):
                A1 = np.matmul(A1, A).astype(np.int64)
                A1 = np.mod(A1, 1000000007)
            A = np.matmul(A1, A1).astype(np.int64)

        else:
            for i in range(int((n - 4) / 2 -1)):
                A1 = np.matmul(A1, A)
                A1 = np.mod(A1, 1000000007)
            A1 = np.matmul(A1, A1)
            A = np.matmul(A, A1)
        A = np.mod(A, 1000000007)
        return int(np.mod(np.matmul(init_array, A)[0], 1000000007))

"""
执行用时：108 ms, 在所有 Python3 提交中击败了99.12% 的用户
内存消耗：29.3 MB, 在所有 Python3 提交中击败了50.50% 的用户
    
解题思路：
    更深入的，我们将二分的快速幂，再细分
    如：  a**8 = ((a**2)**2)**2      
    如：  a**7 = a*((a**2)**2)
    
    例：  a**n
            n = 6时       偶数，计算当前次方      记录奇数
        n = 6               a                 
        n = 6 >> 1 = 3      a**2 = a**2         a**2   
        n = 3 >> 1 = 1      a**2 = a**4 
        
                                    a**4 * a**2 = a**6
        
            n = 7时       n**7 
        n = 7               a                   a
        n = 7 >> 1 = 3      a**2 = a**2         a**2
        n = 3 >> 1 = 1      a**2 = a**4         
        
                                    a**4 * a * a**2 = a**7
                                    
            n = 15时      n**15      
        n = 15               a                   a
        n = 15 >> 1 = 7     a**2 = a**2          a**2
        n = 7 >> 1 = 3      a**2 = a**4          a**4
        n = 3 >> 1 = 1      a**2 = a**8          
        
                                    a**8 * a * a**2 * a**4 = a**15 
    可以看出，n依次除以2向下取整，并对a累次方，
        当遇到n为奇数时，记录当前次方数，
        最后将最终的次方数与 奇数时记录的 所有相乘即可
    
    具体实现见代码注释
"""
import numpy as np

class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        init_array = np.array([4, 2, 1], dtype=np.int64)
        A = np.array([[1, 1, 0], [1, 0, 1], [1, 0, 0]]).astype(np.int64)

        A = self.mat_pow(A, n-3)
        init_array = np.matmul(init_array, A).astype(np.int64)[0]
        return int(init_array % 1000000007)

    def mat_pow(self, A, n):
        e = np.eye(3, dtype=np.int64)  # 用于累计 奇数时的 次方乘积
        while n > 0:
            if (n & 1) != 0:    # 判断奇偶
                e = np.matmul(e, A)    # 当是奇数时， 累计当前次方乘积
                e = np.mod(e, 1000000007)   # 取模
            A = np.matmul(A, A).astype(np.int64)    # 计算当前次方和
            A = np.mod(A, 1000000007)
            n = n >> 1  # /2向下取整
        return e</code></pre></div>
