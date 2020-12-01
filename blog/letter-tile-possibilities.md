Leetcode 1079. 活字印刷
<p>你有一套活字字模&nbsp;<code>tiles</code>，其中每个字模上都刻有一个字母&nbsp;<code>tiles[i]</code>。返回你可以印出的非空字母序列的数目。</p>


<p><strong>注意：</strong>本题中，每个活字字模只能使用一次。</p>



<p>&nbsp;</p>



<p><strong>示例 1：</strong></p>



<pre><strong>输入：</strong>&quot;AAB&quot;

<strong>输出：</strong>8

<strong>解释：</strong>可能的序列为 &quot;A&quot;, &quot;B&quot;, &quot;AA&quot;, &quot;AB&quot;, &quot;BA&quot;, &quot;AAB&quot;, &quot;ABA&quot;, &quot;BAA&quot;。

</pre>



<p><strong>示例 2：</strong></p>



<pre><strong>输入：</strong>&quot;AAABBC&quot;

<strong>输出：</strong>188

</pre>



<p>&nbsp;</p>



<p><strong>提示：</strong></p>



<ol>

	<li><code>1 &lt;= tiles.length &lt;= 7</code></li>

	<li><code>tiles</code> 由大写英文字母组成</li>

</ol>





 **难度**: Medium



 **标签**: 回溯算法、 





<div class="hcb_wrap">
<pre class="prism undefined-numbers lang-python" data-lang="Python"><code>
# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：120 ms, 在所有 Python3 提交中击败了63.74% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了14.45% 的用户

解题思路：
    参考了思路：https://leetcode-cn.com/problems/letter-tile-possibilities/solution/hui-su-suan-fa-python-dai-ma-by-liweiwei1419/
    这哥们写的是真的棒！

    例：  'AAB'
        A   B   AA  AB  BA  AAB ABA BAA
        可见，题目不是排序题，是组合题。
        先统计每个字母出现的次数，然后进行处理
    具体实现见代码。
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []

        tile_dic = {}   # 统计字母出现的次数 {字母:个数}
        for tile in tiles:
            if tile not in tile_dic:
                tile_dic[tile] = 1
            else:
                tile_dic[tile] += 1

        def backtrack(current, tile_dic):   # 传入当前字母个数的字典，以及一个保存当前结果的列表
            # print(current)
            result.append(current[:])   # 每次的当前结果均是最终结果的一部分，所以直接添加到最终结果中
            for tile, n in tile_dic.items():    # 从字典中拿取一个个数大于0的字母
                if n > 0:
                    current.append(tile)    # 放入当前结果中
                    tile_dic[tile] -= 1     # 字母个数-1
                    backtrack(current, tile_dic)
                    current.pop()   # 回溯
                    tile_dic[tile] += 1 # 回溯，字母个数+1
        backtrack([], tile_dic)
        return len(result)-1    # 由于[] 也是最终结果的一部分，所以需要-1
</code></pre></div>
