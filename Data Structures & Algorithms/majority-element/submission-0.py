class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count=defaultdict(int)
        maxcount,res=0,0
        for n in nums:
            count[n]=1+count.get(n,0)
            if count[n] > maxcount:
                maxcount=count[n]
                res = n
        return res
        