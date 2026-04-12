class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        word_set = set(wordDict)
        #print(n)
        def backtrack(idx, curlist):
            if idx == n:
                res.append(" ".join(curlist))
                return

            for end in range(idx, n):
                cur = s[idx : end + 1] 
                if cur in word_set:
                    #print(cur, idx," ", end," ",end+1)
                    curlist.append(cur)
                    backtrack(end + 1, curlist) 
                    curlist.pop()
        #print(res)
        backtrack(0,[])
        return res