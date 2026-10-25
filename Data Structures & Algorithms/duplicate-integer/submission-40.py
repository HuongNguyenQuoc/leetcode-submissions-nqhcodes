class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNum = set(nums)
        return len(nums) != len(setNum)