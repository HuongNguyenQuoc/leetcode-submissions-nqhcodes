class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        
        index = 0
        for num in range(3):
            for _ in range(count[num]):
                nums[index] = num
                index += 1
        