import collections

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_dict = collections.defaultdict(int)
        for word in words:
            words_dict[word] +=1
        
        words_dict = sorted(words_dict.items(), key=lambda x: (-x[1], x[0]))
        words_dict = collections.OrderedDict(words_dict)
        
        top_words = []
        i = 1
        
        for key in words_dict.keys():
            if i <= k:
                top_words.append(key)
                i += 1
        
        return top_words