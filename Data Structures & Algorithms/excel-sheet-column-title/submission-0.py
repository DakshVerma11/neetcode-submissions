class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num=columnNumber
        
        res=[]
        while num:
            num-=1
            res.append(chr(num%26+ord("A")))
            num//=26
        res.reverse()
        return ''.join(res)

