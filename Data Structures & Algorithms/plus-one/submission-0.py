class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add=1
        idx=len(digits)-1

        while idx>=0:
            if digits[idx]==9:
                digits[idx]=0
                idx-=1
            else:
                digits[idx]+=1
                break
        return [1]+digits if idx==-1 else digits
        
            