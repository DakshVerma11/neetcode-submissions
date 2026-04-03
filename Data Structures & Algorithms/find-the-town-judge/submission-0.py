class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
            
        trust_scores = [0] * (n + 1)

        for person, trusted_person in trust:
            trust_scores[person] -= 1
            trust_scores[trusted_person] += 1
        
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1

