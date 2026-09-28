class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if abs(target) > sum(nums):
            return 0
        
        # dp = {0: 1} -> 0 : count
        dp = {0: 1}

        for num in nums:
            next_dp = {}
            for total, count in dp.items():
                next_dp[total] = next_dp.get(next_dp[total], 0) + count
            dp = next_dp
        
        return dp[target]

