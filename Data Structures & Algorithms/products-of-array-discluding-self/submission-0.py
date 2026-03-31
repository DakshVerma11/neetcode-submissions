class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zero=0
        for n in nums:
            if n==0:
                zero+=1
                continue
            prod*=n
        if zero>1:
            nums=[0]*len(nums)
            return nums
        
        for i in range(len(nums)):
            if zero:
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=prod
            else:
                nums[i]=int(prod/nums[i])

        return nums
