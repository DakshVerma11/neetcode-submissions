class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        steps = 0

        while left != right:
            left >>= 1
            right >>= 1
            steps += 1

        return left << steps