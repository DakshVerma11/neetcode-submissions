class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        res=r

        def canSplit(largest):
            noOfArrays=1
            curSum=0
            for num in nums:
                curSum += num
                if curSum > largest:
                    noOfArrays += 1
                    if noOfArrays > k:
                        return False
                    curSum = num
            return True


        while l<=r:
            mid=l+(r-l)//2
            if canSplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1

        return res
        


        