class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdict={0:1}
        count=0
        curSum=0

        for n in nums:
            curSum+=n
            count+=sumdict.get(curSum-k,0)
            sumdict[curSum]=1+sumdict.get(curSum,0)
        return count
