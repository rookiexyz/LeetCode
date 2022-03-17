class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            return pow(x, n//2) ** 2
        else:
            return x * pow(x, n-1)