class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''i=1
        j=max(piles)
        res=j
        while i<=j:
            m=i+(j-i)//2
            time=0
            for i in piles:
                time+=math.ceil(i / m)
            
            if time==h:
                return m
            elif time<h:
                res=m
                j=m-1
            else:
                i=m+1
        return res'''
        i = 1
        j = max(piles)
        res = j

        while i <= j:
            m = i + (j - i) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            
            if time <= h:
                res = m
                j = m - 1
            else:
                i = m + 1

        return res





            