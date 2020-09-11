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