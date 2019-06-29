class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        
        for j in t:
            d[j] -= 1
        
        for k in d.keys():
            if d[k] != 0:
                return False
        return True