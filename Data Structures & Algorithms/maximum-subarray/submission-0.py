class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=min(nums)

        curmax=0
        for i in nums:
            curmax+=i
            res=max(curmax,res)
            if curmax<0:
                curmax=0
            

        return res