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
    
#Time Complexity: O(logN)
#Space Complexity: O(logN)
'''
# Ex with 2^10, First we has 4^5 = (2^2)^5 and then 4^5 will be 16^2 = (4^2)^2 don't worry about here after we calc need expression we'll check if n % 2 we will multiply current_res by x else just return current_res okay, and after that we will have the result we need
'''
    