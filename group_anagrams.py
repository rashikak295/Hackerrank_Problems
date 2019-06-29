import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        
        out = []
        
        for key in groups.keys():
            out.append(groups[key])
            
        return out