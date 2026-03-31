# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n
        while l<=r:
            num=l+(r-l)//2
            match guess(num):
                case 0:
                    return num
                case 1:
                    l=num+1
                case -1:
                    r=num-1
        return l+(r-l)//2