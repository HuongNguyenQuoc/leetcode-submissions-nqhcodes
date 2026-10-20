class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfNumber(n)
        while slow != fast and fast != 1:
            slow = self.sumOfNumber(slow)
            fast = self.sumOfNumber(self.sumOfNumber(fast))
        return fast == 1

    def sumOfNumber(self, n: int) -> int:
        total = 0
        while n:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total