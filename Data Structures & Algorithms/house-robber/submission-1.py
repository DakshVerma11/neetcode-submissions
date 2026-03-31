class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        rob1=nums[0]
        rob2=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            rob1, rob2=rob2, max(rob1+nums[i],rob2)
        return rob2