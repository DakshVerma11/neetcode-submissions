class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def backtracking(i, cur):
            if i == n:
                res.append(cur.copy())
                return
            
            #Include nums[i]
            cur.append(nums[i])
            backtracking(i + 1, cur)
            cur.pop()
            
            #Exclude nums[i]
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
                
            backtracking(i + 1, cur)
            
        backtracking(0, [])
        return res