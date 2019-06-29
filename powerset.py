class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def sub(out, nums):
            if len(nums)==0:
                output.append(out)
            elif len(nums)==1:
                sub(out,[])
                sub(out+[nums[0]],[])   
            elif len(nums)>1:
                sub(out,nums[1:])
                sub(out+[nums[0]],nums[1:])
        
        output = []
        out = []
        sub(out,nums)
        return output