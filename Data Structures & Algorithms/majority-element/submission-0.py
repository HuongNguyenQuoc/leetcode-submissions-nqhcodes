class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for val, freq in counter.items():
            if freq > (len(nums) // 2):
                return val