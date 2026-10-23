class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        dq = deque()
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digit = digits[i] + carry
            dq.appendleft(digit % 10)
            carry = digit // 10
        if carry:
            dq.appendleft(1)
        return list(dq)