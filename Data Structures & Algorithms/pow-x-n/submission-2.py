class Solution:
    def helper(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        res = self.helper(x*x, n // 2)
        return res * x if n % 2 else res
        
    def myPow(self, x: float, n: int) -> float:
        res = self.helper(x, abs(n))
        return res if n >= 0 else 1 / res
    