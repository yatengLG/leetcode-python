# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：32 ms, 在所有 Python3 提交中击败了99.63% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了12.97% 的用户

解题思路：
    先将链表拆分为单个节点，并统计链长度
    根据链表长度以及k，计算，每段的节点个数以及多余的节点数
    按照计算结果连接链表
    具体实现见代码注释
"""
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        record = [] # 列表保存拆分成单个的节点
        r = root
        num = 0     # 统计链表长度
        while r:    # 拆分链表节点
            r_next = r.next
            r.next = None
            record.append(r)
            r = r_next
            num += 1

        result = [] # 最终结果
        remainder = num % k # 计算分段后的多余节点数
        n = num // k    # 每段的个数
        if n < 1:
            return record + [None] * (k - num)

        start_index = 0 # 起始位置
        for i in range(k):
            if remainder > 0:   # 如果还有多余的节点，则前几段每段多一个节点
                nodes = record[start_index:start_index + n + 1]
                start_index += n + 1
                remainder -= 1  # 多余节点数-1
            else:
                nodes = record[start_index:start_index + n]
                start_index += n

            nodes += [None]
            for j, node in enumerate(nodes):    # 重组每段链表
                if node:
                    node.next = nodes[j + 1]
            result.append(nodes[0]) # 将重组后的每段链表添加到最终结果中
        return result