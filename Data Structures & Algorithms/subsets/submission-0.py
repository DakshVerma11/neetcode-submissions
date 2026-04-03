class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        def backtracking(idx,cur):
            if idx>=len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[idx])
            #print(cur)
            backtracking(idx+1,cur)
            cur.pop()
            backtracking(idx+1,cur)
        backtracking(0,[])
        return res