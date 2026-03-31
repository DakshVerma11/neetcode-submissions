class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(numset)==len(nums):
            return False
        return True