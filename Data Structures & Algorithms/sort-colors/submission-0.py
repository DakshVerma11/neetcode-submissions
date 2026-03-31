class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3  # For 0, 1, 2
        for num in nums:
            count[num] += 1

        i = 0
        for val in range(3):
            for _ in range(count[val]):
                nums[i] = val
                i += 1