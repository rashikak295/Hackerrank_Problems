import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_  = sys.maxint
        shortest = ""
        for i in strs:
            if len(i)<min_:
                min_ = len(i)
                shortest = i
        
        for j in strs:
            for k in range(len(shortest)):
                if j[k] != shortest[k]:
                    shortest = shortest[0:k]
                    break
        return shortest
                    