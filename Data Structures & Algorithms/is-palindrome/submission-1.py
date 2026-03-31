class Solution:
    def isPalindrome(self, s: str) -> bool:
        chrs=[]

        for i in s:
            if i.isalnum():
                chrs.append(i.lower())
        lench=len(chrs)
        #print(chrs)
        for i in range(lench//2):
            if chrs[i]!=chrs[lench-1-i]:
                return False
        return True