class Solution:
    def palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        res, cur = [], []

        def backtracking(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    cur.append(s[i : j + 1])
                    backtracking(j + 1)
                    cur.pop()

        backtracking(0)
        return res