class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days>=len(weights):
            return max(weights)
        
        def calculateDays(capacity):
            count=1
            cur=0
            for p in weights:
                cur+=p
                if cur/capacity>1:
                    cur=p
                    count+=1
            return count

        i=max(weights)
        j=sum(weights)
        res=j
        while i<=j:
            m=i+(j-i)//2
            #print('m=',m,'  ','  i=',i,' j=',j,'  ',calculateDays(m))
            if calculateDays(m)<=days:
                j=m-1
                if m<res:
                    res=m
            else:
                i=m+1
        return res