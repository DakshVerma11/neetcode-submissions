class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,cur):

            if sum(cur)==target:
                res.append(cur.copy())
                return
            if i>len(nums)-1 or sum(cur)>target:
                return
            
            cur.append(nums[i])
            backtrack(i,cur)
            cur.pop()
            backtrack(i+1,cur)
        backtrack(0,[])
        return res