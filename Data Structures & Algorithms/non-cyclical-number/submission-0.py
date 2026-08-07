class Solution:
    def isHappy(self, n: int) -> bool:
        

        def sumSqDigits(num):
            res=0
            while num:
                res+=(num%10)**2
                num//=10
            return res
        sumSet=set([1])

        #print(n,sumSqDigits(n))
        while n not in sumSet:
            sumSet.add(n)
            n=sumSqDigits(n)
        return n==1