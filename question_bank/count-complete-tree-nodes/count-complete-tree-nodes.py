# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：64 ms, 在所有 Python3 提交中击败了99.87% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了36.57% 的用户

解题思路：
    参考了官方解题：https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/wan-quan-er-cha-shu-de-jie-dian-ge-shu-by-leetco-2/
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def get_h(root, h): # 获取树高，完全二叉树遍历左子树即可
            if root:
                h = get_h(root.left, h) + 1
            return h

        def exist_node(val, h, root):   # 判断当前节点是否存在
            num = 2 ** (h - 2)
            while num > 0:
                if num & val > 0:
                    root = root.right
                else:
                    root = root.left
                num = num >> 1
            return root is not None

        h = get_h(root, 0)  # 获取当前树高
        if h == 0:
            return 0
        elif h == 1:
            return 1

        num = 2 ** (h - 1)  # 用于记录节点数
        l, r = 2 ** (h - 1), 2 ** h - 1 # 左右指针，分别指向最后一层最左侧节点与最右侧节点(假设存在)
        while l <= r:   # 二分查找
            mid = (r + l) // 2  # # 中间值
            if exist_node(mid, h, root):    # 如果当前mid位置存在节点
                num = mid   # 更新节点数
                l = mid + 1 # 左指针右移
            else:
                r = mid - 1 # 否则，右指针左移
        return num