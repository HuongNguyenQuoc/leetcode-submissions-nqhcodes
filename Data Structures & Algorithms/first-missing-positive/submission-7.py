class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1
        for num in nums:
            if missing != num:
                return missing
            missing += 1
        
        return missing
        