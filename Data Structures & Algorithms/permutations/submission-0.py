class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtracking(taken,cur):
            nonlocal n
            if sum(taken)==n:
                res.append(cur.copy())
                return
            
            for i in range(n):
                if taken[i]:
                    continue
                taken[i]=True
                cur.append(nums[i])
                backtracking(taken,cur)
                taken[i]=False
                cur.pop()
        backtracking([False]*n,[])
        return res
