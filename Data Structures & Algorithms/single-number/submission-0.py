class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numset=set()
        for i in nums:
            if i in numset:
                numset.remove(i)
            else:
                numset.add(i)
        return numset.pop()