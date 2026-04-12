class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False


        sideLen=sum(matchsticks)//4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def backtrack(idx):
            if idx == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for side in range(4):
                if sides[side]+matchsticks[idx]<=sideLen:
                    sides[side] += matchsticks[idx]
                    if backtrack(idx + 1):
                        return True
                    sides[side] -= matchsticks[idx]

            return False
        

        return backtrack(0)
            