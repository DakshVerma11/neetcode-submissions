class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res=[]

        def backtracking(num,cur):
            if len(cur)==k:
                res.append(cur.copy())
                return
            if num>n:
                return
            
            for i in range(num,n+1):
                cur.append(i)
                backtracking(i+1,cur)
                cur.pop()
        backtracking(1,[])
        return res