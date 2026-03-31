class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        res=j
        while i<=j:
            m=i+(j-i)//2
            time=0
            for __ in piles:
                time+=math.ceil(__ / m)
            
            if time<=h:
                res=m
                j=m-1
            else:
                i=m+1
                
        return res
