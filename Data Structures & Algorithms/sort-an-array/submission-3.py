import random
class Solution:
    def quickSort(self, nums, low, high):
        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot_index - 1)
            self.quickSort(nums, pivot_index + 1, high)

    def partition(self, nums, low, high):
        rand_idx = random.randint(low, high)
        nums[high], nums[rand_idx] = nums[rand_idx], nums[high]  # random pivot
        pivot = nums[high]
        j = low - 1
        for i in range(low, high):
            if nums[i] <= pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[j + 1], nums[high] = nums[high], nums[j + 1]
        return j + 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
