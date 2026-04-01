class Solution:
    def reverseBits(self, n: int) -> int:
        temp=0

        for i in range(32):
            print(n&1,end='')
            temp+=n&1
            n>>=1
            temp<<=1
        temp>>=1
        return temp