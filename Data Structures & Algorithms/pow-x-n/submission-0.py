class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickPower(base: float, exponent: int) -> float:
            result = 1.0
            while exponent:
                if exponent & 1:
                    result *= base
                base *= base
                exponent >>= 1
            return result

        return quickPower(x, n) if n >= 0 else 1 / quickPower(x, -n)