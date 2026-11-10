class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0] * 1001
        for a, b, c in trips:
            res[b] += a
            res[c] -= a
        
        currSum = 0
        for _ in range(len(res)):
            currSum += res[_]
            if currSum > capacity:
                return False
        return True