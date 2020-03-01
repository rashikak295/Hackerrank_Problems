import collections
import heapq 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        nums_dict = collections.defaultdict(int)
        for n in nums:
            nums_dict[n] += 1    
        nums_dict = [(V, K) for K, V in nums_dict.items()]
        
        out = nums_dict[0:k] 
        heapq.heapify(out)
        
        for i in range(k,len(nums_dict)):
            if nums_dict[i][0] > out[0][0]:
                heapq.heappushpop(out, nums_dict[i])
                
        return_ = []
        for o in out:
            return_.append(o[1])
        
        return return_        
