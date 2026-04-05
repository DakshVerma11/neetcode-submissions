class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]

        nums.sort()

        n=len(nums)
        def backtracking(i):
            if i == n:
                res.append(nums.copy())
                return

            for j in range(i,n):
                if j>i and nums[i] == nums[j]:
                    continue
                nums[i],nums[j]=nums[j],nums[i]
                backtracking(i+1)

            for j in range(n - 1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]
        backtracking(0)
        return res

