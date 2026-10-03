class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            val = float('inf')
            for l, r in intervals:
                if l <= q <= r:
                    val = min(val, r-l+1)
            if val == float('inf'):
                val = -1
            res.append(val)
        return res