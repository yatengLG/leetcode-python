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