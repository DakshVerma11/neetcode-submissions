class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        zeroidx=-1
        prod=1
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
                zeroidx=i
            else:
                prod*=nums[i]
        

        if zero>1:
            return [0]*len(nums)
        elif zero==1:
            res=[0]*len(nums)
            res[zeroidx]=prod
            return res
        else:
            res=[0]*len(nums)
            for i in range(len(res)):
                res[i]=int(prod/nums[i])
                
            return res