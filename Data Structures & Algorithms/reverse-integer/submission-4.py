class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x, 10)) # Here we need use math.fmod because with negative number it's will cell so it will never hit the 0, ex: -123 % 10 = -3 it will have the same with the signed of origin number
            x = int(x / 10)
            if (res > int(MAX // 10)) or (res == int(MAX // 10) and digit > 7):
                return 0
            elif (res < int(MIN // 10)) or (res == int(MIN // 10) and digit < 8):
                return 0
            res = res * 10 + digit
        return res