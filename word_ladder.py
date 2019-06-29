import collections
import Queue
# from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def neighbours(word):
            l = set()
            for w in range(len(word)):
                temp = word[:w]+'*'+word[w+1:]
                # temp = list(word)
                # temp[w] = '*'
                # temp = ''.join(temp)
                l.add(temp)
            return l
        
        words = collections.defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                temp = list(w)
                temp[i] = '*'
                temp = ''.join(temp)
                words[temp].add(w)
        
        q = Queue.Queue(maxsize=len(wordList)+1)
        # queue = deque(["Eric", "John", "Michael"])
        q_d = collections.defaultdict(int)
        q_d[beginWord] = 1
        step = 1
        q.put((beginWord,step))
        while(not q.empty()):
            p,step = q.get()
            if p == endWord: return step
            neighbour = neighbours(p)
            for n in neighbour:
                for word in words[n]:
                    if word not in q_d.keys():
                        q_d[word] = 1
                        q.put((word,step+1))
        return 0