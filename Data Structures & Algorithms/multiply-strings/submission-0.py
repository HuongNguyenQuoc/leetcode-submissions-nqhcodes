class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(n-1, -1, -1):
            digit1 = ord(num2[i]) - ord('0')

            for j in range(m-1, -1, -1):
                digit2 = ord(num1[j]) - ord('0')

                p1 = i+j
                p2 = i+j+1

                total = digit1 * digit2 + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10
            
        return ''.join(map(str, res)).lstrip('0')