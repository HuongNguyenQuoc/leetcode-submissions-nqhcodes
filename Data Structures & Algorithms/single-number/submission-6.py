from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for value, freq in counter.items():
            if freq == 1:
                return value