class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
            
        a = abs(n)
        res = 1
        for i in range(a):
            res *= x
        return res if n >= 0 else 1 / res
            