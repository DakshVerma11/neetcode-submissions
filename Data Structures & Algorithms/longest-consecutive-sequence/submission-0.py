class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for n in numset:
            if n-1 not in numset:
                current = n
                curlen = 0

                while n in numset:
                    curlen+=1
                    n+=1

                longest=max(longest,curlen)

        return longest