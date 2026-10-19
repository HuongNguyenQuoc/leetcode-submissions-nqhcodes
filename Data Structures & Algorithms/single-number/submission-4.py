class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    nums.pop(j)
                    continue
        return nums.pop()