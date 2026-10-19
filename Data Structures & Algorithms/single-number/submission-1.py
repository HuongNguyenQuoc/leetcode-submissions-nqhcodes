class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        findOne = set()
        for n in nums:
            if n in findOne:
                findOne.remove(n)
                continue
            findOne.add(n)
        
        return int(findOne)