class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        n=len(digits)
        def backtracking(idx,cur):
            if len(cur)==n:
                if cur:
                    res.append("".join(cur))
                return 
            
            opt=digitToChar[digits[idx]]

            for i in opt:
                cur.append(i)
                backtracking(idx+1,cur)
                cur.pop()
        
        backtracking(0,[])
        return res