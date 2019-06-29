import sys
import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min = sys.maxint
        out = []
        dicti = collections.defaultdict(list)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dicti[list1[i]] = [i,j]
                    if i+j<min:
                        min = i+j
        for k in dicti.keys():
            if dicti[k][0] + dicti[k][1] == min:
                out.append(k)
        return out
                