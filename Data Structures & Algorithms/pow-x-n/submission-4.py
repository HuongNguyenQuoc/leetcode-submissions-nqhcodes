class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        
        while n > 0:
            if n % 2:
                res *= x
            
            x *= x
            n //= 2
        
        return res