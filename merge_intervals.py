from operator import itemgetter
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=itemgetter(0))
        length = len(intervals)
        l = 1
        while l < length and l>0:
            if l<len(intervals):
                if intervals[l][0]<=intervals[l-1][1]:
                    if intervals[l][1]<=intervals[l-1][1]:
                        del intervals[l]
                        l = l-1
                    else:
                        intervals[l][0]=intervals[l-1][0]
                        del intervals[l-1]
                        l = l-1
            l = l+1                
        return intervals
            
        