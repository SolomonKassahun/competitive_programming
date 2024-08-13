class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        eleent = None
        for num in nums:
            if count == 0:
                eleent = num
            count += (1 if num == eleent else -1)

        return eleent
            
        