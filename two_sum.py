class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
            else: return [d[nums[i]],i]