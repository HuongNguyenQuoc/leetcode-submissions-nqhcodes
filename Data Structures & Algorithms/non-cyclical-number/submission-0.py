class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        visit.add(n)
        while n:
            n = self.sumSquare(n)
            if n in visit:
                return False
            elif n == 1:
                return True
            visit.add(n)
            
    def sumSquare(self, n: int) -> int:
        sum = 0
        while n:
            tempt = n
            n //= 10
            du = tempt % 10
            sum += du ** 2
        return sum
