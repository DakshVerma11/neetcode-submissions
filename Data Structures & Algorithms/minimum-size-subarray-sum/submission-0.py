class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        minarr=len(nums)
        l=0
        r=0
        
        while r<=len(nums):
            sums=0
            for i in range(l,r):
                sums+=nums[i]
            
            if sums>=target:
                minarr=min(minarr,r-l)
                l+=1
            else:
                r+=1

        return minarr